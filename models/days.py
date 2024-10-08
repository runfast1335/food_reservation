from odoo import models, fields



class Days(models.Model):
    _name = "food_reservation.days"
    _rec_name = "date"


    date = fields.Date(string="تاریخ", required=True, help="تاریخی که میخواهید غذا سفارش دهید را انتخاب کنید")
    poloyi_id = fields.Many2one("food_reservation.foods",string="پولویی", required=True,
                                domain=[('food_type', '=', 'poloyi')])
    khorack_id = fields.Many2one("food_reservation.foods",string="خوراک", required=True,
                                 domain=[('food_type', '=', 'khorack')])
    day_off = fields.Boolean()

    _sql_constraints = [('unique_date', 'unique (date)', 'قبلا برای امروز برنامه غذایی مشخص کرده اید')]







