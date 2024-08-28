# models/project.py

from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    prioridad = fields.Selection(
        [('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')],
        string='Prioridad',
        default='media',
        help="Indica la prioridad del proyecto (Alta, Media, Baja)."
    )
