﻿var controlUrl = '/Admin/FrameworkModules/DataItemAdmin/';

$(function () {    
    pageSizeControl.init({ gridId: 'dicGrid', gridType: 'treegrid' });
    $(window).resize(function () {        
        pageSizeControl.init({ gridId: 'dicGrid', gridType: 'treegrid' });
    });

    DicCategory.bindTree();
    autoResize({ treegrid: '#dicGrid', gridType: 'treegrid', callback: mygrid.databind, height: 35, width: 203 });

    $('#a_addCategory').click(DicCategory.addCategory);
    $('#a_delCategory').click(DicCategory.delCategory);
    $('#a_editCategory').click(DicCategory.editCategory);

    //字典数据
    $('#a_itemdetailadd').click(mygrid.add);
    $('#a_itemdetailedit').click(mygrid.edit);
    $('#a_itemdetaildelete').click(mygrid.del);
    $('#a_refresh').click(function () {
        var node = DicCategory.getSelected();
        if (node)
            mygrid.reload(node.id);
        else {
            msg.warning('请选择字典类别。');
        }
    });
});

var DicCategory = {
    bindTree: function () {
        $('#dataDicType').tree({
            url: controlUrl + 'GetDataItemTreeJson/?isTree=1',
            onLoadSuccess: function (node, data) {
                if (data.length == 0) {
                    $('#noCategoryInfo').fadeIn();
                }

                $('body').data('categoryData', data);
            },
            onClick: function (node) {
                $(this).tree('toggle', node.target);
                var cc = node.id;
                $('#dicGrid').treegrid({
                    url: controlUrl + 'GetDataItemDetailById/',
                    queryParams: { categoryId: cc }
                });
            }
        });
    },
    reload: function () {
        $('#dataDicType').tree('reload');
    },
    getSelected: function () {
        return $('#dataDicType').tree('getSelected');
    },
    bindCtrl: function (curId) {
        var treeData = $('body').data('categoryData');
        treeData = JSON.stringify(treeData);
        treeData = '[{"id":0,"selected":true,"text":"请选择上级节点"},' + treeData.substr(1, treeData.length - 1);

        top.$('#parentid').combotree({
            data: JSON.parse(treeData),
            valueField: 'id',
            textField: 'text',
            panelWidth: '280',
            editable: false,
            lines: true,
            onSelect: function (item) {
                var nodeId = top.$('#parentid').combotree('getValue');
                if (item.id == curId) {
                    top.$('#parentid').combotree('setValue', nodeId);
                    top.$.messager.alert('警告提示', '上级节点不能与当前所选相同！', 'warning');
                }
            }
        }).combotree('setValue', 0);
    },
    addCategory: function () {
        var addDialog = top.$.hDialog({
            title: '添加字典类别',
            iconCls: 'icon16_add',
            href: '/Admin/FrameworkModules/DataItemAdmin/DataItem/?n=' + Math.random(),
            width: 390,
            height: 350,
            onLoad: function () {
                DicCategory.bindCtrl();
                top.$('#enabled').attr("checked", true);
                pageMethod.bindCategory('category', 'DataDictionaryCategory');
            },
            submit: function () {
                var isValid = top.$('#ItemsForm').form("validate");
                if (isValid) {
                    var queryString = pageMethod.serializeJson(top.$('#ItemsForm'));
                    $.ajaxjson(controlUrl + 'SubmitItemsForm/', queryString, function (d) {
                        if (d.Data > 0) {
                            msg.ok('字典类别添加成功。');
                            addDialog.dialog('close');
                            DicCategory.reload();
                        } else {
                            MessageOrRedirect(d);
                        }
                    });
                }
            }
        });
    },
    editCategory: function () {
        var node = DicCategory.getSelected();
        if (node) {
            var editDialog = top.$.hDialog({
                title: '编辑字典类别',
                iconCls: 'icon16_edit_button',
                href: '/Admin/FrameworkModules/DataItemAdmin/DataItem/?n=' + Math.random(),
                width: 390,
                height: 350,
                onLoad: function () {
                    pageMethod.bindCategory('category', 'DataDictionaryCategory');
                    var parm = 'key=' + node.id;
                    $.ajaxjson(controlUrl + 'GetItemsEntity/', parm, function (data) {
                        if (data) {
                            DicCategory.bindCtrl(data.id);
                            SetWebControls(data, true);
                            top.$('#parentid').combotree('setValue', data.parentid);
                        }
                    });
                },
                submit: function () {
                    var isValid = top.$('#ItemsForm').form("validate");
                    if (isValid) {
                        var queryString = pageMethod.serializeJson(top.$('#ItemsForm'));
                        $.ajaxjson(controlUrl + 'SubmitItemsForm/?key=' + node.id, queryString, function (d) {
                            if (d.Data > 0) {
                                msg.ok('亲，字典类别编辑成功啦。');
                                editDialog.dialog('close');
                                DicCategory.reload();
                            } else {
                                MessageOrRedirect(d);
                            }
                        });
                    }
                }
            });
        } else {
            msg.warning('亲,请选择字典类别。');
        }
    },
    delCategory: function () {
        var node = DicCategory.getSelected();
        var rows = $('#dicGrid').treegrid('getData');
        if (rows && rows.length > 0) {
            msg.warning('当前字典有明细数据，不能删除。<br> 请先删除明细数据。');
            return false;
        }
        if (node) {
            if (confirm('亲,确认要删除此类别吗?')) {
                $.ajaxjson(controlUrl + 'DeleteDataItem/', 'key=' + node.id, function (d) {
                    if (d.Data > 0) {
                        msg.ok('亲，字典类别删除成功。');
                        DicCategory.reload();
                    } else {
                        MessageOrRedirect(d);
                    }
                });
            }
        } else {
            msg.warning('亲,请选择字典。');
        }
        return false;
    }
};

var dicDialog;
var mygrid = {
    databind: function(winSize) {
        $('#dicGrid').treegrid({
            toolbar: '#toolbar',
            title: "数据字典明细",
            iconCls: 'icon16_table',
            width: winSize.width,
            height: winSize.height,
            nowrap: false, //折行
            rownumbers: true, //行号
            striped: true, //隔行变色
            idField: 'id', //主键
            treeField: 'itemname',
            singleSelect: true, //单选          
            columns: [
                [
                    { title: 'ItemId', field: 'itemid', hidden: true },
                    { title: 'ParentId', field: 'parentid', hidden: true },
                    { title: 'ID', field: 'id', width: 60, hidden: true },
                    { title: '名称', field: 'itemname', width: 170 },
                    { title: '编码', field: 'itemcode', width: 130 },
                    { title: '值', field: 'itemvalue', width: 130 },
                    { title: '排序', field: 'sortcode', width: 40 },
                    {
                        title: '有效',
                        field: 'enabled',
                        width: 40,
                        formatter: function(v, d, i) {
                            return '<img src="/Content/images/' + (v == '1' ? 'checkmark.gif' : 'checknomark.gif') + '" />';
                        },
                        align: 'center'
                    },
                    {
                        title: '公共',
                        field: 'ispublic',
                        width: 40,
                        formatter: function(v, d, i) {
                            return '<img src="/Content/images/' + (v == '1' ? 'checkmark.gif' : 'checknomark.gif') + '" />';
                        },
                        align: 'center'
                    },
                    {
                        title: '允许编辑',
                        field: 'allowedit',
                        width: 40,
                        formatter: function(v, d, i) {
                            return '<img src="/Content/images/' + (v == '1' ? 'checkmark.gif' : 'checknomark.gif') + '" />';
                        },
                        align: 'center'
                    },
                    {
                        title: '允许删除',
                        field: 'allowdelete',
                        width: 40,
                        formatter: function(v, d, i) {
                            return '<img src="/Content/images/' + (v == '1' ? 'checkmark.gif' : 'checknomark.gif') + '" />';
                        },
                        align: 'center'
                    },
                    { title: '描述', field: 'description', width: 200 }
                ]
            ],
            pagination: false
        });
    },
    reload: function(cc) {
        $('#dicGrid').treegrid({
            url: controlUrl + 'GetDataItemDetailById/',
            queryParams: { categoryId: cc }
        });
    },
    GetSelectedRow: function() {
        return $('#dicGrid').treegrid('getSelected');
    },
    initCtrl: function(dicId) {
        var cateData = $('body').data('categoryData');
        //alert(JSON.stringify(cateData));
        var comboCategory = top.$('#itemid').combobox({ data: cateData.rows, valuefield: 'id', textfield: 'text', editable: false, required: true, missingMessage: '请选择类别', disabled: true });
        var cnode = DicCategory.getSelected();
        if (cnode)
            comboCategory.combobox('setValue', cnode.id);

        var dicData = $("#dicGrid").treegrid('getData');
        if (dicData.length > 0) {
            dicData = JSON.stringify(dicData).replace(/id/g, "id").replace(/itemname/g, "text");
            dicData = '[{id:0,text:"== 请选择 =="},' + dicData.substr(1);
        } else
            dicData = '[{id:0,text:"== 请选择 =="}]';

        var parentTree = top.$('#parentid').combotree({
            data: eval(dicData),
            valuefield: 'id',
            textField: 'text',
            editable: false,
            onSelect: function(item) {
                var nodeId = parentTree.combotree('getValue');
                if (item.id == dicId) {
                    parentTree.combotree('setValue', nodeId);
                    top.$.messager.alert('警告提示', '上级不能与当前字典相同！', 'warning');
                    return false;
                }
            }
        });

        var crow = mygrid.GetSelectedRow();
        if (!dicId && crow) {
            top.$('#parentid').combotree('setValue', crow.Id);
        } else
            top.$('#parentid').combotree('setValue', 0);
    },
    add: function() {
        if ($(this).linkbutton('options').disabled == true) {
            return false;
        }
        if (!DicCategory.getSelected()) {
            msg.warning('请选择字典类别！');
            return false;
        }

        dicDialog = top.$.hDialog({
            href: '/Admin/FrameworkModules/DataItemAdmin/DataItemDetail/?n=' + Math.random(),
            width: 400,
            height: 400,
            title: '新增选项明细',
            iconCls: 'icon16_table_add',
            onLoad: function() {
                mygrid.initCtrl();
                top.$(":checkbox").attr("checked", true); //界面上的所有checkbox默认选中（有效、公共、允许编辑、允许删除）
            },
            submit: function() {
                if (top.$('#dicForm').form('validate')) {
                    var queryString = pageMethod.serializeJson(top.$('#ItemDetailForm'));
                    $.ajaxjson(controlUrl + 'SubmitItemsDetailForm/', queryString, function (d) {
                        if (d.Data > 0) {
                            msg.ok(d.Message);
                            mygrid.reload(top.$('#itemid').combobox('getValue'));
                        } else {
                            MessageOrRedirect(d);
                        }
                    });
                }
            }
        });
        return false;
    },
    edit: function() {
        if ($(this).linkbutton('options').disabled == true) {
            return false;
        }
        var row = mygrid.GetSelectedRow();
        if (row == null) {
            msg.warning("请选择字典数据。");
            return false;
        }
        dicDialog = top.$.hDialog({
            href: '/Admin/FrameworkModules/DataItemAdmin/DataItemDetail/?n=' + Math.random(),
            width: 400,
            height: 400,
            title: '编辑字典',
            iconCls: 'icon16_table_edit',
            onLoad: function() {
                var parm = 'key=' + row.id;
                $.ajaxjson(controlUrl + 'GetItemsDetailEntity/', parm, function (data) {
                    if (data) {
                        mygrid.initCtrl(row.Id);
                        top.$('#parentid').combotree('setValue', row.parentid);
                        SetWebControls(data, true);
                    }
                });
            },
            submit: function() {
                if (top.$('#ItemDetailForm').form('validate')) {
                    var queryString = pageMethod.serializeJson(top.$('#ItemDetailForm'));
                    $.ajaxjson(controlUrl + 'SubmitItemsDetailForm/?key=' + row.id, queryString, function (d) {
                        if (d.Data > 0) {
                            msg.ok(d.Message);
                            mygrid.reload(top.$('#itemid').combobox('getValue'));
                            dicDialog.dialog('close');
                        } else {
                            MessageOrRedirect(d);
                        }
                    });
                }
            }
        });
        return false;
    },
    del: function() {
        if ($(this).linkbutton('options').disabled == true) {
            return false;
        }
        var row = mygrid.GetSelectedRow();
        if (row) {
            var childs = $('#dicGrid').treegrid('getChildren', row.id);
            if (childs.length > 0) {
                msg.warning('当前字典有下级数据，不能删除。<br> 请先删除子节点数据。');
                return false;
            }

            if (confirm('确认要删除此条字典数据吗?')) {
                var query = 'key=' + row.id;
                $.ajaxjson(controlUrl + 'DeleteItemDetail/', query, function (d) {
                    if (d.Data == 1) {
                        msg.ok(d.Message);
                        var node = DicCategory.getSelected();
                        if (node)
                            mygrid.reload(node.id);
                    } else {
                        MessageOrRedirect(d);
                    }
                });
            }
        } else {
            msg.warning('请选中要删除的字典数据。');
        }
        return false;
    }
};