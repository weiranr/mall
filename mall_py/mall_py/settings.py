"""
Django settings for mall_py project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^97w_!e%%xt8tz*4!&1*nuiypz!io2(^m&z_8p&f2lx6!s4v%t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'simpleui',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mall.apps.MallConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mall_py.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mall_py.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mall',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, 'static')),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -----simpleui配置区-----

SIMPLEUI_LOGO = 'http://127.0.0.1:8088/static/image/logo/logo.jpg'
SIMPLEUI_HOME_INFO = False      # 服务器信息
SIMPLEUI_HOME_QUICK = True      # 快速操作
SIMPLEUI_HOME_ACTION = True     # 最近动作
SIMPLEUI_HOME_ANALYSIS = False  # 收集分析，一天只上报一次分析数据。默认为True
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['用户管理', '商品管理', '订单管理', '首页管理', '权限认证'],      # 'XXX管理'  开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
        'app': 'mall',
        'name': '用户管理',
        'icon': 'fa fa-users',
        'models': [{
            'name': '用户信息',
            'icon': 'fa fa-address-card',
            'url': 'mall/malluser/'
        }, {
            'name': '用户地址',
            'icon': 'fa fa-map-marked-alt',
            'url': 'mall/useraddress/'
        }, {
            'name': '用户token',
            'icon': 'fa fa-key',
            'url': 'mall/usertoken/'
        }]
        },
        {
        'app': 'mall',
        'name': '商品管理',
        'icon': 'fas fa-sitemap',
        'models': [{
            'name': '商品信息',
            'icon': 'fa fa-info',
            'url': 'mall/goodsinfo/'
        }, {
            'name': '商品分类',
            'icon': 'fa fa-qrcode',
            'url': 'mall/goodscategory/'
        }, {
            'name': '商品评价',
            'icon': 'fa fa-comments',
            'url': 'mall/mallcomment/'
        }, {
            'name': '购物车',
            'icon': 'fa fa-shopping-cart',
            'url': 'mall/shoppingcart/'
        }]
        },
        {
        'app': 'mall',
        'name': '订单管理',
        'icon': 'fas fa-list-ul',
        'models': [{
            'name': '订单',
            'icon': 'fa fa-clipboard-list',
            'url': 'mall/mallorder/'
        }, {
            'name': '订单项',
            'icon': 'fa fa-info',
            'url': 'mall/orderitem/'
        }, {
            'name': '订单地址',
            'icon': 'fa fa-map-marked-alt',
            'url': 'mall/orderaddress/'
        }]
        },
        {
            'app': 'mall',
            'name': '首页管理',
            'icon': 'fas fa-home',
            'models': [{
                'name': '首页广告',
                'icon': 'fa fa-bullhorn',
                'url': 'mall/mallcarousel/'
            }, {
                'name': '首页设置',
                'icon': 'fa fa-cog',
                'url': 'mall/indexconfig/'
            }]
        },
        {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }, {
            'name': '组',
            'icon': 'fa fa-users',
            'url': 'auth/group/'
        }]
        }
    ]
}

# ------------Django REST Framework配置---------------
REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    # 'PAGE_SIZE': 10
}

# ------------ django-cors-headers配置---------------
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
