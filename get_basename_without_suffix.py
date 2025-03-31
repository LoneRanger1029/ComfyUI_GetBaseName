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

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "output_file_path": ("STRING", {"multiline": False, "default": ""}),
                "file_name": ("STRING", {"multiline": False, "default": ""}),
                "operation_system": (["linux", "mac", "windows"])
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    OUTPUT_NODE = False
    FUNCTION = 'save_text_to_file'
    CATEGORY = 'Tools'

    def save_text_to_file(self, text, output_file_path, file_name, operation_system):

        if output_file_path.endswith('/') or output_file_path.endswith('\\'):
            output_file_path = output_file_path[:-1]

        if operation_system == 'windows':
            filepath = output_file_path + "\\" + file_name + ".txt"
        else:
            filepath = output_file_path + "/" + file_name + ".txt"

        if output_file_path == "" or file_name == "":
            print(f"[Warning] Save Text List. No file details found. No file output.")
            return ()

        print(f"[Info] Save Text : Saving to {filepath}")

        with open(filepath, 'w', encoding='utf-8') as file:
            try:
                file.write(text)
            except Exception as e:
                print(f"[Error] Save Text Error: {e}")

        return ()

NODE_CLASS_MAPPINGS = {
    "GetBasenameWithoutSuffix": GetBasenameWithoutSuffix,
    "SaveTextToFile": SaveTextToFile
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetBasenameWithoutSuffix": "Get Basename Without Suffix",
    "SaveTextToFile": "Save Text To File"
}
