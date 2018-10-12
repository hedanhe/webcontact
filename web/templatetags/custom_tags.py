from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def tree_search(d_dic, comment_obj):
    for k,v_dic in d_dic.items():
        if comment_obj.parent_comment == k:
            d_dic[k][comment_obj] = {}
            return
        else:
            tree_search(d_dic[k], comment_obj)

def generate_html(sub_comment_dic, margin_left_value):
    html = ""
    for k,v_dic in sub_comment_dic.items():

        html += "<div class='comment-node' style='margin-left:%spx'>"% margin_left_value + k.comment + "</div>"
        if v_dic:
            html += generate_html(v_dic, margin_left_value+15)
    return html

@register.simple_tag
def build_comment_tree(comment_list):

    comment_dic = {}
    for comment_obj in comment_list:
        if comment_obj.parent_comment is None:
            comment_dic[comment_obj] = {}

        else:
            tree_search(comment_dic, comment_obj)


    margin_left_value = 0

    html = "<div class='comment-box'>"
    for k,v in comment_dic.items():
        if not v:
            html += "<div class='comment-node_li'>" + k.comment + "</div>"
        else:
            html += "<div class='comment-node_li'>" + k.comment
        html += generate_html(v, margin_left_value+15)

    html += "</div>"

    return mark_safe(html)



