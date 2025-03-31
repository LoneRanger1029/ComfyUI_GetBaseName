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
        """获得无后缀的文件名称, 参数名需要和上面 required 对应"""
        basename = os.path.basename(file_path)
        return (basename[:basename.rfind('.')],)


class SaveTextToFile:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "multiline_text": ("STRING",),
                "file_path": ("STRING",)
            }
        }

    RETURN_TYPES = ()  # 即使没有返回值也应该返回空元组
    RETURN_NAMES = ()  # 即使没有返回值也应该返回空元组
    FUNCTION = "save_text_to_file"
    CATEGORY = "Tools"

    def save_text_to_file(self, multiline_text, file_path):
        """
        :param multiline_text: 图片对应的标签值
        :param file_path: 图片的文件全路径
        """
        try:
            dir_path = os.path.dirname(file_path)
            file_name = os.path.basename(file_path)
            basename = file_name[: file_name.rfind('.')]
            full_path = os.path.join(dir_path, basename + ".txt")
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(multiline_text)
        except Exception as e:
            print(f"写入文件时出错: {e}")
        return ()  # 即使没有返回值也应该返回空元组


NODE_CLASS_MAPPINGS = {
    "GetBasenameWithoutSuffix": GetBasenameWithoutSuffix,
    "SaveTextToFile": SaveTextToFile
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetBasenameWithoutSuffix": "Get Basename Without Suffix",
    "SaveTextToFile": "Save Text To File"
}
