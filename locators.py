class Locators(object):
    logo = '.logo > img'
    calculation_link = 'Calculate delivery cost'
    submit_form_button = '.text-center.hidden-xs > .submit-calculation-form'

    country_empty_field = '#calculation-form > div.has-error > p'
    shipping_empty_method = '#calculation-form > div.has-error > p'
    weight_empty_field = '#calculation-form > div.has-error > p'

    shipping_cost = '.cost-of-delivery'
    total_cost = '.summary-calculation'

    all_shipping_types = '#calculatedeliveryform-shipping_type > option'
    select_country = '#calculatedeliveryform-country.form-control'
    select_ukraine = '#calculatedeliveryform-country > option[value="1"]'

    select_shipping_method = '#calculatedeliveryform-shipping_method'

    select_shipping_type = '#calculatedeliveryform-shipping_type.form-control'
    shipping_type_dropdown_default = '#calculatedeliveryform-shipping_type > option[value="-1"'

    county_error = '.form-group.field-calculatedeliveryform-country.required > p'
    shipping_method_error = '.form-group.field-calculatedeliveryform-shipping_method.required > p'
    shipping_type_error = '.field-calculatedeliveryform-shipping_type > .help-block-error'
    weight_error = '.form-group.field-calculatedeliveryform-weight.required > p'

    weight_field = '#calculatedeliveryform-weight'



