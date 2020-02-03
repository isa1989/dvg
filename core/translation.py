from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MenuTranslationOption(TranslationOptions):
    fields = ('name',)


class ModalMenuTranslationOption(TranslationOptions):
    fields = ('name',)


class OurFocusTranslationOption(TranslationOptions):
    fields = ('title', 'content',)


class WhatWeDoTranslationOption(TranslationOptions):
    fields = ('title', 'title_main', 'content',)


class ManifestoTranslationOption(TranslationOptions):
    fields = ('title_bold', 'title_plane',)


class JoinUsTranslationOption(TranslationOptions):
    fields = ('title_bold',)


class WorkShopTranslationOption(TranslationOptions):
    fields = ('name', 'title_bold', 'title_plane', 'title_main_bold', 'title_main_plane', 'content_bold',
              'content_plane',)


class SettingsTranslationOption(TranslationOptions):
    fields = ('home_page_title', 'home_title_bold', 'home_title_plane', 'home_title_button_manifesto',
              'home_title_button_url', 'home_we_garner', 'home_our_focus', 'home_partners', 'footer_title',
              'footer_links', 'footer_home_link', 'footer_home_url', 'footer_whatwedo_link', 'footer_whatwedo_url',
              'footer_manifesto_link', 'footer_manifesto_url', 'footer_joinus_link', 'footer_joinus_url',
              'footer_contact_us', 'footer_contact_us_adress', 'copyright', 'cases_title', 'cases_banking',
              'cases_bold_title_banking', 'cases_plane_title_banking', 'cases_bold_content_banking',
              'cases_plane_content_banking', 'cases_insurance', 'cases_bold_title_insurance',
              'cases_plane_title_insurance', 'cases_bold_content_insurance', 'cases_plane_content_insurance',
              'cases_telecom', 'cases_bold_title_telecom', 'cases_plane_title_telecom', 'cases_bold_content_telecom',
              'cases_plane_content_telecom', 'cases_startup', 'cases_bold_title_startup', 'cases_plane_title_startup',
              'cases_bold_content_startup', 'joinus_title', 'index_title', 'not_found_title', 'not_found_opps',
              'not_found_name', 'not_found_content', 'not_found_url', 'not_found_path', 'index_title_manifesto',
              'index_title_workshop', 'logo_header_url', 'logo_home_url', 'logo_footer_url')


translator.register(Menu, MenuTranslationOption)
translator.register(ModalMenu, ModalMenuTranslationOption)
translator.register(OurFocus, OurFocusTranslationOption)
translator.register(WhatWeDo, WhatWeDoTranslationOption)
translator.register(Manifesto, ManifestoTranslationOption)
translator.register(JoinUs, JoinUsTranslationOption)
translator.register(WorkShop, WorkShopTranslationOption)
translator.register(Settings, SettingsTranslationOption)
