from django.db import models
from django.contrib.auth.models import User

class Websites(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    base_id = models.CharField(max_length=250, null=True, blank=True)
    table_id = models.CharField(max_length=250, null=True, blank=True)
    require_login = models.BooleanField(default=False, null=True, blank=True)
    email_selector = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    password_selector = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    button_selector = models.CharField(max_length=250, null=True, blank=True)
    no_pagination = models.BooleanField(default=False, null=True, blank=True)
    pagination_click = models.CharField(max_length=250, null=True, blank=True)
    pagination_path = models.CharField(max_length=250, null=True, blank=True)
    product_selector = models.CharField(max_length=250, null=True, blank=True)
    not_contains_class = models.CharField(max_length=250, null=True, blank=True)
    inner_selector = models.CharField(max_length=250, null=True, blank=True)
    inside_category_selector = models.CharField(max_length=250, null=True, blank=True)
    product_click = models.BooleanField(default=False, null=True, blank=True)
    title_prefix = models.CharField(max_length=250, null=True, blank=True)
    ar_title_prefix = models.CharField(max_length=250, null=True, blank=True)
    title_prefix_selector = models.CharField(max_length=250, null=True, blank=True)
    title_prefix_attr = models.CharField(max_length=250, null=True, blank=True)
    title_selector = models.CharField(max_length=250, null=True, blank=True)
    title_attr = models.CharField(max_length=250, null=True, blank=True)
    title_suffix = models.CharField(max_length=250, null=True, blank=True)
    title_suffix_selector = models.CharField(max_length=250, null=True, blank=True)
    title_suffix_attr = models.CharField(max_length=250, null=True, blank=True)
    description_selector = models.CharField(max_length=250, null=True, blank=True)
    description_attr = models.CharField(max_length=250, null=True, blank=True)
    key_words_selector = models.CharField(max_length=250, default="meta[property*='og:title']")
    main_img_selector = models.CharField(max_length=250, null=True, blank=True)
    main_img_attr = models.CharField(max_length=250, null=True, blank=True, default="src")
    img_click = models.BooleanField(default=False, null=True, blank=True)
    img_selector = models.CharField(max_length=250, null=True, blank=True)
    img_attr = models.CharField(max_length=250, null=True, blank=True, default="src")
    static_price = models.CharField(max_length=250, null=True, blank=True)
    is_price_have_comma = models.BooleanField(default=False, null=True, blank=True)
    price_selector = models.CharField(max_length=250, null=True, blank=True)
    price_attr = models.CharField(max_length=250, null=True, blank=True)
    second_price_selector = models.CharField(max_length=250, null=True, blank=True)
    second_price_attr = models.CharField(max_length=250, null=True, blank=True)
    is_discount = models.BooleanField(default=False, null=True, blank=True)
    discount_selector = models.CharField(max_length=250, null=True, blank=True)
    discount_attr = models.CharField(max_length=250, null=True, blank=True)
    is_stuck = models.BooleanField(default=False, null=True, blank=True)
    stuck_selector = models.CharField(max_length=250, null=True, blank=True)
    is_feature = models.BooleanField(default=False, null=True, blank=True)
    features_selector = models.CharField(max_length=250, null=True, blank=True)
    features_key_selector = models.CharField(max_length=250, null=True, blank=True)
    features_key_attr = models.CharField(max_length=250, null=True, blank=True)
    features_value_selector = models.CharField(max_length=250, null=True, blank=True)
    features_value_attr = models.CharField(max_length=250, null=True, blank=True)
    en_link = models.CharField(max_length=250, null=True, blank=True)
    ar_link = models.CharField(max_length=250, null=True, blank=True)
    ar_selector = models.CharField(max_length=250, null=True, blank=True)
    ar_attr = models.CharField(max_length=250, null=True, blank=True, default="href")
    export_out_of_stuck = models.BooleanField(default=False, null=True, blank=True)
    start_index = models.IntegerField(default=1, null=True, blank=True)
    end_index = models.IntegerField(null=True, blank=True)
    number_of_products = models.IntegerField(null=True, blank=True)
    change_content = models.BooleanField(default=True)
    translate_english = models.BooleanField(default=True)
    translate_arabic = models.BooleanField(default=True)

class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    api_status = models.CharField(max_length=250, null=True, blank=True)