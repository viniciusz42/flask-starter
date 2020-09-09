from datetime import datetime


def sum_freelancer_hours(payload):
    """ Sum freelancer skill experience hours

    Args:
        payload (dict): request payload

    Returns:
        dict: freelancer total skills hours computed
    """

    freelance = payload.get('freelance')
    freelancer_id = freelance.get('id')
    experiences = freelance.get('professionalExperiences')
    computed_xp = list()
    skills = dict()

    for xp in experiences:
        start, end = _extract_range(xp)
        months = (end.year - start.year) * 12 + (end.month - start.month)
        overlap, overlapped_skills = _find_overlaps(_extract_range(xp), computed_xp)

        for skill in xp.get('skills'):
            id = skill.get('id')
            skills[id] = dict(
                id=id,
                name=skill.get('name'),
                durationInMonths=_sum_durations(id, months, skills, overlap, overlapped_skills)
            )

        computed_xp.append(xp)

    return dict(
        freelance=dict(
            id=freelancer_id,
            computedSkills=list(skills.values())
        )
    )

def _calc_overlap_months(range1, range2):
    """ Calculates overlap in months between two ranges

    Args:
        range1 (datetime): first range
        range2 (datetime) second range

    Returns:
        int: overlap in months
    """

    start1, end1 = range1
    start2, end2 = range2
    months = 0

    if start1 <= end2 and end1 >= start2:
        diff = min(end2, end1) - max(start2, start1)
        months = round(diff.days / 30)

    return months


def _extract_range(experience):
    """ Extract dates from dictionary
    and convert them to datetime

    Args:
        experience (dict): experience

    Returns:
        tuple: start and end date
    """

    start = datetime.fromisoformat(experience.get('startDate'))
    end = datetime.fromisoformat(experience.get('endDate'))
    return start, end


def _find_overlaps(experience_range, computed_xp):
    """ Iterates over computed experiences
    in order to find overlapsing date ranges

    Args:
        experience_range (tuple): current experience range
        computed_xp (dict) computed experiences

    Returns:
        tuple: overlap in months and a list of skill ids
    """

    overlapped_skills = []
    overlap = 0

    for xp in computed_xp:
        overlap = _calc_overlap_months(experience_range, _extract_range(xp))
        if overlap > 0:
            overlapped_skills.append([skill.get('id') for skill in xp.get('skills')])

    return overlap, overlapped_skills


def _sum_durations(id, months, skills, overlap, overlapped_skills):
    """ Sums total amount of experience hours a freelancer
    has with one skill

    Args:
        id (int): skill id
        months (dict) experience in months
        skills (dict) skills
        overlap (int) overlap in months
        overlapped_skills (list) list of overlapped skill ids
    Returns:
        int: adjusted duration of experience at one skill
    """
    duration = months

    if id in skills:
        duration = skills[id]['durationInMonths'] + months
        if id not in overlapped_skills:
            duration = duration - overlap

    return duration




