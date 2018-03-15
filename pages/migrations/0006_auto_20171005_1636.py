# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 16:36
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171005_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='body',
            field=wagtail.core.fields.StreamField((('single_column', wagtail.core.blocks.StructBlock((('column', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('background_color', pages.models.BackgroundColorBlock())), group='COLUMNS')), ('two_columns', wagtail.core.blocks.StructBlock((('left_column', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('right_column', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('background_color', pages.models.BackgroundColorBlock())), group='COLUMNS')), ('four_columns', wagtail.core.blocks.StructBlock((('left_column_1', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('left_column_2', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('right_column_1', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('right_column_2', wagtail.core.blocks.StreamBlock((('h1', wagtail.core.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.core.blocks.CharBlock(classname='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('lead_body', wagtail.core.blocks.CharBlock(classname='lead')), ('small_text', wagtail.core.blocks.CharBlock(classname='small')), ('blockquote', wagtail.core.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('icon', wagtail.core.blocks.StructBlock((('font_awesome_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.core.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('background_color', pages.models.BackgroundColorBlock())), group='COLUMNS')), ('starfish', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()),))), ('hero_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alternate_text', wagtail.core.blocks.CharBlock(help_text='Text for screen readers')), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption will be shown below the image', max_length=120, required=False)), ('fine_print', wagtail.core.blocks.CharBlock(help_text='Fine Print will be shown below caption', max_length=120, required=False)), ('overlay_text', wagtail.core.blocks.BooleanBlock(help_text='If checked, caption is overlayed on image', required=False)), ('photo_credit', wagtail.core.blocks.CharBlock(help_text='This will show bottom right on the image', max_length=80, required=False))), icon='image'))), default=''),
        ),
    ]
