# -*- coding: utf-8 -*-
import os
import geonode

# Setting debug to true makes Django serve static media and
# present pretty error pages.
#DEBUG = TEMPLATE_DEBUG = False
#DEBUG = TEMPLATE_DEBUG = True

# Set to True to load non-minified versions of (static) client dependencies
# Requires to set-up Node and tools that are required for static development
# otherwise it will raise errors for the missing non-minified dependencies
DEBUG_STATIC = False

SITENAME = 'GeoNode'
#SITEURL = 'http://tiny-ki-geo.vm/'
SITEURL = 'http://192.168.56.32/'

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geonode_data',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

GEOSERVER_URL = SITEURL + 'geoserver/'

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://localhost:8080/geoserver/',
        'USER' : '',
        'PASSWORD' : '',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : True,
        'LOG_FILE':'/var/log/tomcat7/geoserver.log',
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
    }
}


# why do these settings not work?
#DEFAULT_MAP_CENTER = (1.4667,173.03) # Kiribati
#DEFAULT_MAP_BASE_LAYER="OSM Pacific Extract"
#DEFAULT_MAP_ZOOM = '11'


# all map base layers in the system
BASELAYERS = {
    "No background":{
            "source": {"ptype": "gxp_olsource"},
            "type": "OpenLayers.Layer",
            "name": "No background",
            "args": ["No background"],
            "visibility": False,
            "fixed": True,
            "group":"background"
        },

        "OSM Pacific Extract":{
            "source": {"ptype": "gxp_olsource"},
            "type":"OpenLayers.Layer.WMS",
            "name": "OSM Pacific Extract",
            "group":"background",
            "visibility": False,
            "fixed": True,
            "args":[
                "OSM Pacific Extract",
                "http://192.168.56.32/geoserver/wms",
                {
                    "layers":["geonode:osm_composite"],
                    "format":"image/png",
                    "bgcolor":"0xb5d0d0",
                    "tiled": True
                }
            ]
        },

        "OSM Kiribati Extract":{
            "source": {"ptype": "gxp_olsource"},
            "type":"OpenLayers.Layer.WMS",
            "name": "OSM Kiribati Extract",
            "group":"background",
            "visibility": False,
            "fixed": True,
            "args":[
                "OSM Kiribati Extract",
                "http://192.168.56.32/geoserver/wms",
                {
                    "layers":["geonode:osm_composite"],
                    "format":"image/png",
                    "bgcolor":"0xb5d0d0",
                    "tiled": True
                }
            ]
        },

        "mapnik":{
            "source": {"ptype": "gxp_osmsource"},
            "type": "OpenLayers.Layer.OSM",
            "name": "mapnik",
            "visibility": False,
            "fixed": True,
            "group": "background"
        },

        "osm":{
            "source": {"ptype": "gxp_mapquestsource"},
            "name": "osm",
            "group": "background",
            "visibility": True
        },

        "naip":{
            "source": {"ptype": "gxp_mapquestsource"},
            "name": "naip",
            "group": "background",
            "visibility": False
        },

        "mapboxsource":{
            "source": {"ptype": "gxp_mapboxsource"}
        }
}


# map base layers we want to appear as options in geonode (HINT: edit this one!)
DEFAULT_MAP_BASELAYERS = ["No background","OSM Pacific Extract"]


# produces MAP_BASELAYER settings
def get_default_map_baselayers():
    maplist = []
    for m in DEFAULT_MAP_BASELAYERS:
      if not BASELAYERS.get(m) is None:
        maplist.append(BASELAYERS.get(m))
    return maplist


MAP_BASELAYERS = get_default_map_baselayers()


LANGUAGE_CODE = 'en'

MEDIA_ROOT = '/var/www/geonode/uploaded'
STATIC_ROOT = '/var/www/geonode/static/'

# secret key used in hashing, should be a long, unique string for each
# site.  See http://docs.djangoproject.com/en/1.2/ref/settings/#secret-key
SECRET_KEY = ''


CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

# A Google Maps API key is needed for the 3D Google Earth view of maps
# See http://code.google.com/apis/maps/signup.html
GOOGLE_API_KEY = ''

# Bing API key needed for bing maps
#BING_API_KEY = ''

GEONODE_ROOT = os.path.dirname(geonode.__file__)

TEMPLATE_DIRS = (
    '/etc/geonode/templates',
    os.path.join(GEONODE_ROOT, 'templates'),
)

# Additional directories which hold static files
STATICFILES_DIRS = [
    '/etc/geonode/media',
    os.path.join(GEONODE_ROOT, 'static'),
]

#REGISTRATION_OPEN = False
#ACCOUNT_APPROVAL_REQUIRED = False

#ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False
#ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False

# Allowed values for the preview library are 'geoext' and 'leaflet'.
#LAYER_PREVIEW_LIBRARY = 'geoext'

# Uncomment the following to receive emails whenever there are errors in GeoNode
# or to be notified of new user requests when ACCOUNT_APPROVAL_REQUIRED has been set.
#ADMINS = (
#            ('John', 'john@example.com'),
#         )

# Uncomment the following to use a Gmail account as the email backend
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'youremail@gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'
#EMAIL_PORT = 587

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings
ALLOWED_HOSTS=['localhost', 'tiny-ki-geo.vm', '127.0.0.1', '192.168.56.32', ]
