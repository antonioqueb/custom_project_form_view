from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    prioridad = fields.Selection(
        [('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')],
        string='Prioridad',
        default='media',
        help="Indica la prioridad del proyecto (Alta, Media, Baja)."
    )

    scrum_master = fields.Many2one(
        'res.users',
        string='Scrum Master',
        help='Referencia al usuario asignado como Scrum Master.'
    )

    product_owner = fields.Many2one(
        'res.users',
        string='Product Owner',
        help='Referencia al usuario asignado como Product Owner.'
    )

    equipo_desarrollo = fields.Many2many(
        'res.users',
        string='Equipo de Desarrollo',
        help='Lista de usuarios asignados como desarrolladores del proyecto.'
    )



    historias_usuario = fields.Many2many(
    'project.user_story',
    string='Historias de Usuario',
    help='Lista de historias de usuario asociadas al proyecto.'
    )

    backlog_producto = fields.Many2one(
    'project.backlog',
    string='Backlog del Producto',
    help='Referencia al backlog del producto vinculado al proyecto.'
    )

    puntos_historia = fields.Integer(
    string='Puntos de Historia',
    help='Estimación de puntos de historia para la tarea o proyecto.'
    )

    estado_sprint = fields.Selection(
    [('en_progreso', 'En Progreso'), ('finalizada', 'Finalizada'), ('pendiente', 'Pendiente')],
    string='Estado del Sprint',
    help='Estado actual de la tarea dentro del sprint.'
    )

    criterios_aceptacion = fields.Text(
    string='Criterios de Aceptación',
    help='Descripción de los criterios de aceptación para la tarea o historia.'
    )

    revisiones_validaciones = fields.Text(
    string='Revisiones y Validaciones',
    help='Información sobre las revisiones y validaciones necesarias.'
    )









