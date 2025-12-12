from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.server.call('level_1')
    anvil.server.call('level_a')
    anvil.server.call('level_a')
    # Any code you write here will run before the form opens.
