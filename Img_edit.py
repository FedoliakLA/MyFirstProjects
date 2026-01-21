from PIL import Image, ImageFilter
from PIL import ImageEnhance
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import os

Form, Window = uic.loadUiType("Img_edit_ui.ui")

app = QApplication([])
Window = Window()
Form = Form()

"""class ImageEditor():
    def __init__(self, file_name):
        self.filename = file_name
        self.original = None
        self.filelist = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайдено!')

    def print_info(self):
        print("Назва оригінального зображення: ", self.filename)
        print("Сьогочасний формат: ", self.original.format)
        print("Сьогочасний розмір: ", self.original.size)
        print("Сьогочасний мод: ", self.original.mod)

    def do_bw(self):
        gray = self.original.convert("L")
        self.filelist.append(gray)
        gray.save("orig_gray.jpg")
        gray.show()

    def do_blur(self):
        blur = self.original.filter(ImageFilter.BLUR)
        self.filelist.append(blur)
        blur.save("orig_blur.jpg")
        blur.show()

    def do_turn_180(self):
        turn = self.original.transpose(Image.ROTATE_180)
        self.filelist.append(turn)
        turn.save("orig_180.jpg")
        turn.show()

    def do_turn_FLR(self):
        FLR = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.filelist.append(FLR)
        FLR.save("orig_FLR.jpg")
        FLR.show()

    def do_contrast(self):
        contr = self.original.ImageEnhance.Contrast(self.original)
        x = int(input("Множник контрасту: "))
        contr = contr.enhance(x)
        contr.save("original_contr.jpg")
        contr.show()"""

wokrdir = ''
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form
        self.ui.setupUi(self)
        self.ui.Folder_pb.clicked.connect(self.showFilenamesList)

        self.workimage = ImageProcessor(self.ui)
        self.ui.Photo_lw.currentRowChanged.connect(self.showChosenImage)

    def chooseWorkdir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory()

    def filter(self, files, extensions):
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

    def showFilenamesList(self):
        extensions = [".bmp", ".jpg", ".gif", ".jpeg", ".png"]
        self.chooseWorkdir()
        filenames = self.filter(os.listdir(workdir), extensions)
        self.ui.Photo_lw.clear()
        for filename in filenames:
            self.ui.Photo_lw.addItem(filename)

    def showChosenImage(self):
        if self.ui.Photo_lw.currentRow() >= 0:
            filename = self.ui.Photo_lw.currentItem().text()
            self.workimage.loadImage(workdir, filename)
            image_path = os.path.join(self.workimage.dir, self.workimage.filename)
            self.workimage.showImage(image_path)


class ImageProcessor:
    def __init__(self, ui):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.ui = ui

        self.ui.Blck_wht_pb.clicked.connect(self.do_bw)
        self.ui.Mirror_pb.clicked.connect(self.do_mirror_flip)
        self.ui.T_left_pb.clicked.connect(self.do_flip_left)
        self.ui.T_right_pb.clicked.connect(self.do_flip_right)
        self.ui.Contrast_pb.clicked.connect(self.do_contrast)
        self.ui.Blur_pb.clicked.connect(self.do_blur)
        self.ui.Smooth_pb.clicked.connect(self.make_smooth)

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        self.ui.label.hide()
        pixmapImage = QPixmap(path)
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmapImage = pixmapImage.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.label.setPixmap(pixmapImage)
        self.ui.label.show()

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_mirror_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_contrast(self):
        note_name, ok = QInputDialog.getText(Project, "Надати множник контрастності", "Множник: ")
        if ok and note_name != "":
            note_name = int(note_name)
            self.image = ImageEnhance.Contrast(self.image)
            self.image = self.image.enhance(note_name)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def make_smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

Project = Widget()
Project.show()

app.exec()