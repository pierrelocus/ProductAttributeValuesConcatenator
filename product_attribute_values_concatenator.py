# -*- coding: utf-8 -*-

for rec in env['product.template'].filtered(lambda k: len(k['attribute_line_ids']['value_ids']) > 1):
    for attribute_line in rec['attribute_line_ids']:
        if len(attribute_line['value_ids']) > 1:
            n_attribute_value = ' / '.join(attribute_line['value_ids'].mapped('name'))
            n_value = env['product.attribute.value'].search([
                ('name', '=', n_attribute_value)
            ])
            if not n_value:
                n_value = env['product.attribute.value'].create({
                    'name': n_attribute_value,
                    'attribute_id': attribute_line['attribute_id']['id']
                })
            attribute_line['value_ids'] = [(6, 0, [n_value.id])]
