from odoo import models, fields, api

class TaskAssignment(models.Model):
    _name = 'task.assignment'
    _description = 'Task Assignment'

    name = fields.Char(string="Task Name", required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string="Assigned To", required=True, tracking=True)
    due_date = fields.Date(string="Due Date", tracking=True)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string="Status", default='pending', tracking=True)
    description = fields.Text(string="Task Description")


