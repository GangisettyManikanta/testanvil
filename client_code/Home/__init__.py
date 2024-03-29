from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    name = anvil.server.call("name")
    app_tables.exp_users.add_row(email=name['email'],password=name['password'])
    self.label_3.text = name['email']
    self.label_5.text = name['password']
    print(name)