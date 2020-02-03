from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Settings(models.Model):
    # # home page settings
    home_page_title = models.CharField(max_length=255, default='Home', )
    home_title_bold = models.CharField(max_length=255, default='Digital Ventures Group', )
    home_title_plane = RichTextField(default='DVG is a common platform where product owners, agile '
                                             'leaders, designers and engineers collaborate to invent, '
                                             'design and develop new products and technologies or '
                                             'upgrade existing digital platforms.', )
    home_title_button_manifesto = models.CharField(max_length=50, default='Manifesto', )
    home_title_button_url = models.CharField(max_length=255)
    home_we_garner = models.TextField()
    home_our_focus = models.CharField(max_length=50, default='Our Focus')
    home_partners = models.CharField(max_length=100, default='Partners')
    # footer settings
    footer_title = models.CharField(max_length=100, default='Digital Ventures Group')
    footer_links = models.CharField(max_length=100, default='Quick links')
    footer_home_link = models.CharField(max_length=50, default='Home')
    footer_home_url = models.CharField(max_length=255)
    footer_whatwedo_link = models.CharField(max_length=50, default='What we do')
    footer_whatwedo_url = models.CharField(max_length=255)
    footer_manifesto_link = models.CharField(max_length=50, default='Manifesto')
    footer_manifesto_url = models.CharField(max_length=255)
    footer_joinus_link = models.CharField(max_length=50, default='Join us')
    footer_joinus_url = models.CharField(max_length=255)
    footer_contact_us = models.CharField(max_length=50, default='Contact us')
    footer_contact_us_adress = models.CharField(max_length=255, default='Baku, AF Business House, floor 5')
    footer_tel_text = models.CharField(max_length=255, default='+994 12')
    footer_email = models.CharField(max_length=255, default='info@dvg.com')
    copyright = models.CharField(max_length=255, default='© Copyright 2020 - DVG. All rights reserved.')
    # sosial network
    facebook = models.CharField(max_length=300, null=True, blank=True, help_text='Example /about/ -page url')
    facebook_target = models.BooleanField(default=True)
    instagram = models.CharField(max_length=300, null=True, blank=True, help_text='Example /about/ -page url')
    instagram_target = models.BooleanField(default=True)
    linkedin = models.CharField(max_length=300, null=True, blank=True, help_text='Example /about/ -page url')
    linkedin_target = models.BooleanField(default=True)
    twitter = models.CharField(max_length=300, null=True, blank=True, help_text='Example /about/ -page url')
    twitter_target = models.BooleanField(default=True)
    mail = models.CharField(max_length=300, null=True, blank=True, help_text='Example /about/ -page url')
    mail_target = models.BooleanField(default=True)
    # logo
    logo_header = models.FileField(null=True, blank=True, upload_to='settings')
    logo_header_url = models.CharField(max_length=300, blank=True, null=True,)
    logo_home = models.FileField(null=True, blank=True, upload_to='settings')
    logo_home_url = models.CharField(max_length=300, blank=True, null=True,)
    logo_footer = models.FileField(null=True, blank=True, upload_to='settings')
    logo_footer_url = models.CharField(max_length=300, blank=True, null=True,)

    # What we do
    index_title = models.CharField(max_length=255, null=True, blank=True, default='What we do')
    # Manifesto
    index_title_manifesto = models.CharField(max_length=255, null=True, blank=True, default='Manifesto')
    # Workshop
    index_title_workshop = models.CharField(max_length=255, null=True, blank=True, default='workshops')
    # What we do cases
    cases_title = models.CharField(max_length=255, null=True, blank=True, default='Cases')
    cases_banking = models.CharField(max_length=300, default='Banking')
    cases_bold_title_banking = models.CharField(max_length=300)
    cases_plane_title_banking = models.TextField()
    cases_bold_content_banking = models.CharField(max_length=300)
    cases_plane_content_banking = models.TextField()

    cases_insurance = models.CharField(max_length=300, default='Insurance')
    cases_bold_title_insurance = models.CharField(max_length=300)
    cases_plane_title_insurance = models.TextField()
    cases_bold_content_insurance = models.CharField(max_length=300)
    cases_plane_content_insurance = models.TextField()

    cases_telecom = models.CharField(max_length=300, default='Telecom')
    cases_bold_title_telecom = models.CharField(max_length=300)
    cases_plane_title_telecom = models.TextField()
    cases_bold_content_telecom = models.CharField(max_length=300)
    cases_plane_content_telecom = models.TextField()

    cases_startup = models.CharField(max_length=300, default='Startup')
    cases_bold_title_startup = models.CharField(max_length=300)
    cases_plane_title_startup = models.TextField()
    cases_bold_content_startup = models.CharField(max_length=300)
    cases_plane_content_startup = models.TextField()
    # Join us
    joinus_title = models.CharField(max_length=255, default='Join us')
    #Not found 404 page
    not_found_title = models.CharField(max_length=300, blank=True, null=True, default='404 - Page not found')
    not_found_opps = models.CharField(max_length=300, blank=True, null=True, default='Oops!')
    not_found_name = models.CharField(max_length=300, blank=True, null=True, default='404 - Page not found')
    not_found_content = models.TextField(blank=True, null=True,)
    not_found_url = models.CharField(max_length=300, blank=True, null=True, default='Go To Homepage')
    not_found_path = models.CharField(max_length=300, blank=True, null=True,)


    def __str__(self):
        return "{}".format("Settings")

    class Meta:
        verbose_name_plural = "Settings"


class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_children(self):
        return Menu.objects.filter(parent=self)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyular'


class ModalMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_children(self):
        return Menu.objects.filter(parent=self)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Modal Menyu'
        verbose_name_plural = 'Modal Menyular'


class OurFocus(models.Model):
    title = models.CharField(max_length=255, default='Innovative solutions')
    content = RichTextField()

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Our Focus'
        verbose_name_plural = 'Our Focus'


class Partners(models.Model):
    image = models.FileField(upload_to='partners')
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.image)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


class WhatWeDo(models.Model):
    title = models.CharField(max_length=300, default='Strategic design & digital empowerment')
    title_main = models.TextField()
    content = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'What we do'
        verbose_name_plural = 'What we do'


class Manifesto(models.Model):
    title_bold = models.CharField(max_length=300, )
    title_plane = models.TextField()

    def __str__(self):
        return '{}'.format(self.title_bold)

    class Meta:
        verbose_name = 'Manifesto'
        verbose_name_plural = 'Manifesto'


class JoinUs(models.Model):
    title_bold = RichTextField()

    def __str__(self):
        return '{}'.format(self.title_bold)

    class Meta:
        verbose_name = 'Join us'
        verbose_name_plural = 'Join us'


class WorkShop(models.Model):
    name = models.CharField(max_length=400)
    title_bold = models.CharField(max_length=400)
    title_plane = models.TextField()
    title_main_bold = models.CharField(max_length=400)
    title_main_plane = models.TextField()
    content_bold = models.CharField(max_length=400)
    content_plane = models.TextField()

    class Meta:
        verbose_name = 'Work shop'
        verbose_name_plural = 'Work shop'
