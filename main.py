import os


class GetBaseName:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            'required': {
                'FILE PATH': ('FILE PATH', {'default': ''})
            }
        }

    RETURN_TYPES = ('STRING')
    RETURN_NAMES = ('basename')
    FUNCTION = 'get_basename'
    CATEGORY = 'Tools'

    def get_basename(self, path):
        return os.path.basename(path)


NODE_CLASS_MAPPINGS = {
    'GetBaseName': GetBaseName
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'GetBaseName': 'Get Basename From Path'
}
