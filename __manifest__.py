# __manifest__.py
{
    'name': 'Custom Project Form View',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Custom module to replace the default project form view',
    'description': 'This module replaces the default form view for the Project model with a custom view.',
    'author': 'Alphaqueb Consulting',
    'website': 'https://www.alphaqueb.com',
    'depends': ['project'],
    'data': [
        'views/project_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
