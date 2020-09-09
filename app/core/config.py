class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


CONFIG_ENV = dict(
    development=DevelopmentConfig,
    test=TestConfig,
    production=ProductionConfig,
)
