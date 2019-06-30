import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication1.xaml')
        
    def Button_Click(self, sender, e):
        pass

    
    def Button_Click1(self, sender, e):
        pass

if __name__ == '__main__':
    Application().Run(MyWindow())

#1