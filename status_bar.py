from openerp import models, fields, api

class thestatusbar(models.Model):

	_name ='statusbar'

	name = fields.Char('Task', required = True)

	state = fields.Selection([
			('start', 'Started'),
			('progress', 'In progress'),
			('done', 'Done'),
			] ,default='start')

	@api.multi
	def startbar(self):
		self.ensure_one()
		self.write({
		'state': 'start'
	})

	@api.multi
	def progressbar(self):
		self.ensure_one()
		self.write({
		'state': 'progress'
	})

	@api.multi
	def donebar(self):
		self.ensure_one()
		self.write({
		'state': 'done'
	})