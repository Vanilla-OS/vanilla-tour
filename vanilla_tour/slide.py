# slide.py
#
# Copyright 2024 Muqtadir
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, GLib
import webbrowser

@Gtk.Template(resource_path="/org/vanillaos/Tour/blp/slide.ui")
class Slide(Adw.Bin):
    __gtype_name__ = "Slide"

    status_page = Gtk.Template.Child()
    assets_svg = Gtk.Template.Child()
    btn_action = Gtk.Template.Child()

    def __init__(self, slide, **kwargs):
        super().__init__(**kwargs)
        self.__slide = slide
        self.__build_ui()

        self.btn_action.connect("clicked", self.__on_btn_action_clicked)

    def __build_ui(self):
        self.assets_svg.set_resource(self.__slide["resource"])
        self.status_page.set_title(self.__slide["title"])
        self.status_page.set_description(self.__slide["description"])

        if "action" in self.__slide:
            self.btn_action.set_visible(True)
            self.btn_action.set_label(self.__slide["action"]["title"])

    def __on_btn_action_clicked(self, widget):
        if self.__slide["action"]["callback"].startswith("url://"):
                webbrowser.open(self.__slide["action"]["callback"].split("url://")[1])

        elif self.__slide["action"]["callback"].startswith("cmd://"):
            GLib.spawn_command_line_async(self.__slide["action"]["callback"].split("cmd://")[1])
 