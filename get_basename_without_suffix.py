import os


class GetBasenameWithoutSuffix:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("basename",)
    FUNCTION = "get_basename"
    CATEGORY = "Tools"

    def get_basename(self, file_path):
        """获得无后缀的文件名称, 参数名需要和上吗 required 对应"""
        basename = os.path.basename(file_path)
        return (basename[:basename.rfind('.')],)


NODE_CLASS_MAPPINGS = {
    "GetBasenameWithoutSuffix": GetBasenameWithoutSuffix
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetBasenameWithoutSuffix": "Get Basename Without Suffix"
}
