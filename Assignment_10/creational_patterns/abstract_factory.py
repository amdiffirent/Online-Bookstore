from abc import ABC, abstractmethod

# Abstract Product Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products for Windows
class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering a Windows checkbox"

# Concrete Products for MacOS
class MacOSButton(Button):
    def render(self):
        return "Rendering a MacOS button"

class MacOSCheckbox(Checkbox):
    def render(self):
        return "Rendering a MacOS checkbox"

# Abstract Factory Interface
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Example usage of the abstract factory
factory = WindowsFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()

print(button.render())
print(checkbox.render())
