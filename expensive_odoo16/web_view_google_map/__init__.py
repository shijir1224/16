# -*- coding: utf-8 -*-
from . import models


def _uninstall_view_google_map(cr, registry):
    cr.execute(
        "UPDATE ir_act_window "
        "SET view_mode=replace(view_mode, ',google_map', '')"
        "WHERE view_mode LIKE '%,google_map%';"
    )
    cr.execute(
        "UPDATE ir_act_window "
        "SET view_mode=replace(view_mode, 'google_map,', '')"
        "WHERE view_mode LIKE '%google_map,%';"
    )
    cr.execute("DELETE FROM ir_act_window WHERE view_mode = 'google_map';")
