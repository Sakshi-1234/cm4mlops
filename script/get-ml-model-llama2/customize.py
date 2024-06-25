from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    path = env.get('LLAMA2_CHECKPOINT_PATH', '').strip()

    if path == '' or not os.path.exists(path):
        env['CM_TMP_REQUIRE_DOWNLOAD'] = 'yes'

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['LLAMA2_CHECKPOINT_PATH'] = env['CM_ML_MODEL_PATH']
    env['CM_ML_MODEL_PATH'] = env['LLAMA2_CHECKPOINT_PATH']
    env['CM_ML_MODEL_LLAMA2_FILE_WITH_PATH'] = env['LLAMA2_CHECKPOINT_PATH']
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_PATH']

    return {'return':0}
