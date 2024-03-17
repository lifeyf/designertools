origin_text = r'''
<TablacusExplorer>
    <Ctrl Type="196608" Left="50%" Top="50%" Width="50%" Height="50%" Visible="1">
        <Ctrl Type="1" Path="D:\project\max2020\previews">
        </Ctrl>
        <Ctrl Type="1" Path="D:\project\max2020\autoback">
        </Ctrl>
        <Ctrl Type="1" Path="E:\material\texture">
        </Ctrl>
        <Ctrl Type="1" Path="E:\material\study">
        </Ctrl>
        <Ctrl Type="1" Path="E:\material\scene">
        </Ctrl>
    </Ctrl>
    <Ctrl Type="196608" Left="0" Top="50%" Width="50%" Height="50%" Visible="1">
        <Ctrl Type="1" Path="{1}\02-Output\Prophase">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\01-Input\Doc">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\01-Input\Feedback">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\01-Input\model">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\01-Input\images">
        </Ctrl>
    </Ctrl>
    <Ctrl Type="196608" Left="50%" Top="0" Width="50%" Height="50%" Visible="1">
        <Ctrl Type="1" Path="{0}\02-Output\3D\cam">
        </Ctrl>
        <Ctrl Type="1" Path="{0}\02-Output\3D\map">
        </Ctrl>
        <Ctrl Type="1" Path="{0}\02-Output\3D\model">
        </Ctrl>
        <Ctrl Type="1" Path="{0}\02-Output\3D\fx">
        </Ctrl>
    </Ctrl>
    <Ctrl Type="196608" Left="0" Top="0" Width="50%" Height="50%" Visible="1">
        <Ctrl Type="1" Path="{1}\02-Output\Vfx\preview">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\02-Output\Vfx\sof">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\02-Output\Vfx\render\layout">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\02-Output\3D\S-frame">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\02-Output\3D\S-frame\镜头单帧">
        </Ctrl>
        <Ctrl Type="1" Path="{1}\02-Output\3D\3D-render">
        </Ctrl>
    </Ctrl>
</TablacusExplorer>
'''
from pathlib import WindowsPath, Path
import winreg
import re


class CreateXML:
    def __init__(self, root:WindowsPath, dest:WindowsPath="", origin_text:str=origin_text):
        self.text = origin_text
        self.root = root
        self.result = self.__get_result(self.root)
        self.dest = dest or self.__desktop_path()

    def __desktop_path(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        desktop = winreg.QueryValueEx(key, "Desktop")[0]
        return WindowsPath(desktop)

    def __get_result(self, root):
        name_exam = re.search(r"\d+-+[a-zA-Z]+-+[a-zA-Z]+-+.+\\?", str(root))
        server_pos = str(root)
        if name_exam:
            project_name = name_exam.group(0).split('\\')[0]
            result_folder = "\\\\192.168.100.249\\myway-projects\\" + project_name
            if Path(result_folder).exists():
                server_pos = result_folder
        return self.text.format(str(root), server_pos)
    
    def __set_file_name(self):
        name_gen = self.root.parts
        file_name = WindowsPath(name_gen[-1] + ".xml")
        # 693-BJ-Aoyuan-002
        name_exam = re.search(r"\d+-+[a-zA-Z]+-+[a-zA-Z]+-+\d*", str(self.root))
        if name_exam:
            file_name = WindowsPath(name_exam.group() + ".xml")
        return self.dest.joinpath(file_name)

    def make(self, dest:WindowsPath=0):
        dest_file = dest or self.__set_file_name()
        with open(dest_file, "w", encoding='utf-8')as f:
            f.write(self.result)
        return dest_file


if __name__=="__main__":
    root = WindowsPath(r"\\192.168.1.249\myway-projects\670-SH-Xinyanindustry-003-1")
    root = WindowsPath(r"\\192.168.1.249\myway-projects\670-SH-Xinyanindustry03-1y-projects\670H-Xinyanindustry-003-1")
    A = CreateXML(root)
    A.make()