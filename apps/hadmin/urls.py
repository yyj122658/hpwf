# _*_ coding: utf-8 _*_
__author__ = 'baxuelong@163.com'
__date__ = '2019/1/4 11:06'
from django.conf.urls import url
import apps.hadmin.views.LoginController_view as LoginController
import apps.hadmin.views.HomeController_view as HomeController
import apps.hadmin.views.FramworkModules.UserAdminController_view as UserAdminController
import apps.hadmin.views.FramworkModules.OrganizeAdminController_view as OrganizeAdmin
import apps.hadmin.views.FramworkModules.StaffAdminController_view as StaffAdmin
import apps.hadmin.views.FramworkModules.RoleAdminController_view as RoleAdmin
import apps.hadmin.views.FramworkModules.PostAdminController_view as PostAdmin
import apps.hadmin.views.FramworkModules.ModuleAdminController_view as ModuleAdmin
import apps.hadmin.views.FramworkModules.PermissionItemAdminController_views as PermissionItem
import apps.hadmin.views.FramworkModules.UserPermissionAdminController_views as UserPermission
import apps.hadmin.views.FramworkModules.RolePermissionAdminController_views as RolePermission
import apps.hadmin.views.FramworkModules.MessageAdminController_view as MessageAdmin
import apps.hadmin.views.FramworkModules.LogAdminController_view as LogAdmin
import apps.hadmin.views.FramworkModules.ExceptionAdminController_view as ExceptionAdmin
import apps.hadmin.views.FramworkModules.DataItemAdminController_view as DataItemAdmin
import apps.hadmin.views.FramworkModules.ParameterAdminController_view as ParameterAdmin
import apps.hadmin.views.FramworkModules.SequenceAdminController_view as SequenceAdmin
import apps.hadmin.views.FramworkModules.TableFieldAdminController_view as TableFieldAdmin
import apps.hadmin.views.FramworkModules.UtilityController_view as Utility
import apps.hadmin.views.FramworkModules.PermissionSetController_view as PermissionSet
import apps.hadmin.views.FramworkModules.ResourcePermissionController_view as ResourcePermission
import apps.hadmin.views.FramworkModules.SysConfigAdminController_view as SysConfig
import apps.hadmin.views.FramworkModules.HighchartsController_view as Highcharts
import apps.hadmin.views.ExampleModules.PDFReaderController_view as PDFReader
import apps.hadmin.views.ExampleModules.CKEditorController_view as CKEditor
import apps.hadmin.views.FramworkModules.DailyBizAdminController_view as DailyBiz
import apps.hadmin.views.FramworkModules.UnClaimedTaskAdminController_view as UnClaimedTask
import apps.hadmin.views.FramworkModules.ToDoTaskAdminController_view as ToDoTask
import apps.hadmin.views.FramworkModules.MyParticipantTaskAdminController_view as MyParticipantTask


urlpatterns = [
    url(r'^Index/', LoginController.Index),
    url(r'^CheckLogin/', LoginController.CheckLogin),
    url(r'^OutLogin/', LoginController.OutLogin),
    url(r'^AccordionTreeIndex/', HomeController.AccordiontreeIndex),
    url(r'^TreeIndex/', HomeController.TreeIndex),
    url(r'^LoadTreeMenu/', HomeController.LoadTreeMenu),
    url(r'^StartPage/', HomeController.StartPage),
    #
    url(r'^FrameworkModules/Utility/GetCategory/', Utility.GetCategory),
    url(r'^FrameworkModules/Utility/ExportExcel/', Utility.ExportExcel),
    url(r'^FrameworkModules/Utility/Search/', Utility.Search),
    #用户管理
    url(r'^FrameworkModules/UserAdmin/Index/', UserAdminController.Index),
    url(r'^FrameworkModules/UserAdmin/GetUserPageDTByDepartmentId/', UserAdminController.GetUserPageDTByDepartmentId),
    url(r'^FrameworkModules/UserAdmin/GetUserListByPage/', UserAdminController.GetUserListByPage),
    url(r'^FrameworkModules/UserAdmin/Form/', UserAdminController.Form),
    url(r'^FrameworkModules/UserAdmin/SubmitForm/', UserAdminController.SubmitForm),
    url(r'^FrameworkModules/UserAdmin/GetEntity/', UserAdminController.GetEntity),
    url(r'^FrameworkModules/UserAdmin/Delete/', UserAdminController.Delete),
    url(r'^FrameworkModules/UserAdmin/SetUserPassword/', UserAdminController.SetUserPassword),
    url(r'^FrameworkModules/UserAdmin/UserDimission/', UserAdminController.UserDimission),
    url(r'^FrameworkModules/UserAdmin/SetUserDimission/', UserAdminController.SetUserDimission),
    url(r'^FrameworkModules/UserAdmin/GetUserListJson/', UserAdminController.GetUserListJson),
    url(r'^FrameworkModules/UserAdmin/GetDTByRole/', UserAdminController.GetDTByRole),
    url(r'^FrameworkModules/UserAdmin/RemoveRoleByUserId/', UserAdminController.RemoveRoleByUserId),
    #组织机构管理
    url(r'^FrameworkModules/OrganizeAdmin/Index/', OrganizeAdmin.Index),
    url(r'^FrameworkModules/OrganizeAdmin/GetOrganizeTreeJson/', OrganizeAdmin.GetOrganizeTreeJson),
    url(r'^FrameworkModules/OrganizeAdmin/GetOrganizeByCategory/', OrganizeAdmin.GetOrganizeByCategory),
    url(r'^FrameworkModules/OrganizeAdmin/Form/', OrganizeAdmin.Form),
    url(r'^FrameworkModules/OrganizeAdmin/SubmitForm/', OrganizeAdmin.SubmitForm),
    url(r'^FrameworkModules/OrganizeAdmin/GetEntity/', OrganizeAdmin.GetEntity),
    url(r'^FrameworkModules/OrganizeAdmin/Delete/', OrganizeAdmin.Delete),
    url(r'^FrameworkModules/OrganizeAdmin/MoveTo/', OrganizeAdmin.MoveTo),
    #员工管理
    url(r'^FrameworkModules/StaffAdmin/Index/', StaffAdmin.Index),
    url(r'^FrameworkModules/StaffAdmin/GetStaffByOrganizeId/', StaffAdmin.GetStaffByOrganizeId),
    url(r'^FrameworkModules/StaffAdmin/Form/', StaffAdmin.Form),
    url(r'^FrameworkModules/StaffAdmin/SubmitForm/', StaffAdmin.SubmitForm),
    url(r'^FrameworkModules/StaffAdmin/GetEntity/', StaffAdmin.GetEntity),
    url(r'^FrameworkModules/StaffAdmin/Delete/', StaffAdmin.Delete),
    url(r'^FrameworkModules/StaffAdmin/MoveTo/', StaffAdmin.MoveTo),
    #角色管理
    url(r'^FrameworkModules/RoleAdmin/Index/', RoleAdmin.Index),
    url(r'^FrameworkModules/RoleAdmin/GridPageListJson/', RoleAdmin.GridPageListJson),
    url(r'^FrameworkModules/RoleAdmin/GetRoleListByOrganize/', RoleAdmin.GetRoleListByOrganize),
    url(r'^FrameworkModules/RoleAdmin/GetRoleCategory/', RoleAdmin.GetRoleCategory),
    url(r'^FrameworkModules/RoleAdmin/GetEnabledRoleList/', RoleAdmin.GetEnabledRoleList),
    url(r'^FrameworkModules/RoleAdmin/Form/', RoleAdmin.Form),
    url(r'^FrameworkModules/RoleAdmin/SubmitForm/', RoleAdmin.SubmitForm),
    url(r'^FrameworkModules/RoleAdmin/GetEntity/', RoleAdmin.GetEntity),
    url(r'^FrameworkModules/RoleAdmin/Delete/', RoleAdmin.Delete),
    url(r'^FrameworkModules/RoleAdmin/AddUserToRole/', RoleAdmin.AddUserToRole),
    url(r'^FrameworkModules/RoleAdmin/RemoveUserFromRole/', RoleAdmin.RemoveUserFromRole),
    url(r'^FrameworkModules/RoleAdmin/GetRoleList/', RoleAdmin.GetRoleList),
    url(r'^FrameworkModules/RoleAdmin/GetRoleListByUserId/', RoleAdmin.GetRoleListByUserId),
    #岗位管理
    url(r'^FrameworkModules/PostAdmin/Index/', PostAdmin.Index),
    url(r'^FrameworkModules/PostAdmin/Form/', PostAdmin.Form),
    url(r'^FrameworkModules/PostAdmin/SubmitForm/', PostAdmin.SubmitForm),
    url(r'^FrameworkModules/PostAdmin/GetEntity/', PostAdmin.GetEntity),
    url(r'^FrameworkModules/PostAdmin/Delete/', PostAdmin.Delete),
    url(r'^FrameworkModules/PostAdmin/MoveTo/', PostAdmin.MoveTo),
    #模块管理
    url(r'^FrameworkModules/ModuleAdmin/Index/', ModuleAdmin.Index),
    url(r'^FrameworkModules/ModuleAdmin/GetModuleTreeJson/', ModuleAdmin.GetModuleTreeJson),
    url(r'^FrameworkModules/ModuleAdmin/GetModuleByIds/', ModuleAdmin.GetModuleByIds),
    url(r'^FrameworkModules/ModuleAdmin/Form/', ModuleAdmin.Form),
    url(r'^FrameworkModules/ModuleAdmin/SubmitForm/', ModuleAdmin.SubmitForm),
    url(r'^FrameworkModules/ModuleAdmin/GetEntity/', ModuleAdmin.GetEntity),
    url(r'^FrameworkModules/ModuleAdmin/Delete/', ModuleAdmin.Delete),
    #操作权限管理
    url(r'^FrameworkModules/PermissionItemAdmin/Index/', PermissionItem.Index),
    url(r'^FrameworkModules/PermissionItemAdmin/GetPermissionItemTreeJson/', PermissionItem.GetPermissionItemTreeJson),
    url(r'^FrameworkModules/PermissionItemAdmin/GetPermissionItemByIds/', PermissionItem.GetPermissionItemByIds),
    url(r'^FrameworkModules/PermissionItemAdmin/Form/', PermissionItem.Form),
    url(r'^FrameworkModules/PermissionItemAdmin/SubmitForm/', PermissionItem.SubmitForm),
    url(r'^FrameworkModules/PermissionItemAdmin/GetEntity/', PermissionItem.GetEntity),
    url(r'^FrameworkModules/PermissionItemAdmin/Delete/', PermissionItem.Delete),
    url(r'^FrameworkModules/PermissionItemAdmin/MoveTo/', PermissionItem.MoveTo),

    #工作流
    url(r'^FrameworkModules/DailyBizAdmin/Index/', DailyBiz.Index),
    url(r'^FrameworkModules/UnClaimedTaskAdmin/Index/', UnClaimedTask.Index),
    url(r'^FrameworkModules/ToDoTaskAdmin/Index/', ToDoTask.Index),
    url(r'^FrameworkModules/MyParticipantTaskAdmin/Index/', MyParticipantTask.Index),

    url(r'^FrameworkModules/UserPermissionAdmin/Index/', UserPermission.Index),
    url(r'^FrameworkModules/RolePermissionAdmin/Index/', RolePermission.Index),
    url(r'^FrameworkModules/MessageAdmin/Index/', MessageAdmin.Index),
    url(r'^FrameworkModules/MessageAdmin/GetMessageListByFunctionCode/', MessageAdmin.GetMessageListByFunctionCode),
    url(r'^FrameworkModules/MessageAdmin/SendMessageForm/', MessageAdmin.SendMessageForm),
    url(r'^FrameworkModules/MessageAdmin/BroadcastMessageForm/', MessageAdmin.BroadcastMessageForm),
    url(r'^FrameworkModules/MessageAdmin/BroadcastMessage/', MessageAdmin.BroadcastMessage),
    url(r'^FrameworkModules/MessageAdmin/OptionUser/', MessageAdmin.OptionUser),
    url(r'^FrameworkModules/MessageAdmin/OptionUserJson/', MessageAdmin.OptionUserJson),
    url(r'^FrameworkModules/MessageAdmin/SendMessage/', MessageAdmin.SendMessage),
    url(r'^FrameworkModules/MessageAdmin/ReadMessage/', MessageAdmin.ReadMessage),
    url(r'^FrameworkModules/MessageAdmin/Delete/', MessageAdmin.Delete),
    url(r'^FrameworkModules/LogAdmin/Index/', LogAdmin.Index),
    url(r'^FrameworkModules/LogAdmin/GridPageListJson/', LogAdmin.GridPageListJson),
    url(r'^FrameworkModules/LogAdmin/LogByUser/', LogAdmin.LogByUser),
    url(r'^FrameworkModules/LogAdmin/GetPageListLogByUser/', LogAdmin.GetPageListLogByUser),
    url(r'^FrameworkModules/LogAdmin/Delete/', LogAdmin.Delete),
    url(r'^FrameworkModules/LogAdmin/LogByGeneral/', LogAdmin.LogByGeneral),
    url(r'^FrameworkModules/LogAdmin/GetPageListLogByGeneral/', LogAdmin.GetPageListLogByGeneral),
    url(r'^FrameworkModules/ExceptionAdmin/Index/', ExceptionAdmin.Index),
    url(r'^FrameworkModules/ExceptionAdmin/GridPageListJson/', ExceptionAdmin.GridPageListJson),
    url(r'^FrameworkModules/ExceptionAdmin/Delete/', ExceptionAdmin.Delete),
    url(r'^FrameworkModules/DataItemAdmin/Index/', DataItemAdmin.Index),
    url(r'^FrameworkModules/DataItemAdmin/GetDataItemTreeJson/', DataItemAdmin.GetDataItemTreeJson),
    url(r'^FrameworkModules/DataItemAdmin/GetDataItemDetailById/', DataItemAdmin.GetDataItemDetailById),
    url(r'^FrameworkModules/DataItemAdmin/DataItemDetail/', DataItemAdmin.DataItemDetail),
    url(r'^FrameworkModules/DataItemAdmin/DataItem/', DataItemAdmin.DataItem),
    url(r'^FrameworkModules/DataItemAdmin/SubmitItemsForm/', DataItemAdmin.SubmitItemsForm),
    url(r'^FrameworkModules/DataItemAdmin/DeleteDataItem/', DataItemAdmin.DeleteDataItem),
    url(r'^FrameworkModules/DataItemAdmin/DeleteItemDetail/', DataItemAdmin.DeleteItemDetail),
    url(r'^FrameworkModules/DataItemAdmin/GetItemsEntity/', DataItemAdmin.GetItemsEntity),
    url(r'^FrameworkModules/DataItemAdmin/GetItemsDetailEntity/', DataItemAdmin.GetItemsDetailEntity),
    url(r'^FrameworkModules/DataItemAdmin/SubmitItemsDetailForm/', DataItemAdmin.SubmitItemsDetailForm),
    url(r'^FrameworkModules/ParameterAdmin/Index/', ParameterAdmin.Index),
    url(r'^FrameworkModules/ParameterAdmin/GridPageListJson/', ParameterAdmin.GridPageListJson),
    url(r'^FrameworkModules/ParameterAdmin/Form/', ParameterAdmin.Form),
    url(r'^FrameworkModules/ParameterAdmin/GetEntity/', ParameterAdmin.GetEntity),
    url(r'^FrameworkModules/ParameterAdmin/SubmitForm/', ParameterAdmin.SubmitForm),
    url(r'^FrameworkModules/ParameterAdmin/Delete/', ParameterAdmin.Delete),
    url(r'^FrameworkModules/SequenceAdmin/GridPageListJson/', SequenceAdmin.GridPageListJson),
    url(r'^FrameworkModules/SequenceAdmin/Index/', SequenceAdmin.Index),
    url(r'^FrameworkModules/SequenceAdmin/Form/', SequenceAdmin.Form),
    url(r'^FrameworkModules/SequenceAdmin/GetEntity/', SequenceAdmin.GetEntity),
    url(r'^FrameworkModules/SequenceAdmin/SubmitForm/', SequenceAdmin.SubmitForm),
    url(r'^FrameworkModules/SequenceAdmin/Delete/', SequenceAdmin.Delete),
    url(r'^FrameworkModules/TableFieldAdmin/Index/', TableFieldAdmin.Index),
    url(r'^FrameworkModules/TableFieldAdmin/GetTableNameAndCode/', TableFieldAdmin.GetTableNameAndCode),
    url(r'^FrameworkModules/TableFieldAdmin/GetDTByTable/', TableFieldAdmin.GetDTByTable),
    #权限设置
    url(r'^FrameworkModules/PermissionSet/RoleUserSet/', PermissionSet.RoleUserSet),
    url(r'^FrameworkModules/PermissionSet/PermissionBacthSet/', PermissionSet.PermissionBacthSet),
    url(r'^FrameworkModules/PermissionSet/GetPermissionScopeTargetIds/', PermissionSet.GetPermissionScopeTargetIds),
    url(r'^FrameworkModules/PermissionSet/GrantRevokePermissionScopeTargets/', PermissionSet.GrantRevokePermissionScopeTargets),
    url(r'^FrameworkModules/PermissionSet/RolePermissionSet/', PermissionSet.RolePermissionSet),
    url(r'^FrameworkModules/PermissionSet/GetModuleByRoleId/', PermissionSet.GetModuleByRoleId),
    url(r'^FrameworkModules/PermissionSet/GetPermissionItemsByRoleId/', PermissionSet.GetPermissionItemsByRoleId),
    url(r'^FrameworkModules/PermissionSet/SetRoleModulePermission/', PermissionSet.SetRoleModulePermission),
    url(r'^FrameworkModules/PermissionSet/SetRolePermissionItem/', PermissionSet.SetRolePermissionItem),
    url(r'^FrameworkModules/PermissionSet/GetModuleByUserId/', PermissionSet.GetModuleByUserId),
    url(r'^FrameworkModules/PermissionSet/SetUserModulePermission/', PermissionSet.SetUserModulePermission),
    url(r'^FrameworkModules/PermissionSet/GetPermissionItemsByUserId/', PermissionSet.GetPermissionItemsByUserId),
    url(r'^FrameworkModules/PermissionSet/SetUserPermissionItem/', PermissionSet.SetUserPermissionItem),
    url(r'^FrameworkModules/PermissionSet/UserPermissionSet/', PermissionSet.UserPermissionSet),
    url(r'^FrameworkModules/PermissionSet/GetUserRoleIds/', PermissionSet.GetUserRoleIds),
    url(r'^FrameworkModules/PermissionSet/AddUserToRole/', PermissionSet.AddUserToRole),
    url(r'^FrameworkModules/PermissionSet/RemoveUserFromRole/', PermissionSet.RemoveUserFromRole),
    url(r'^FrameworkModules/PermissionSet/UserRoleSet/', PermissionSet.UserRoleSet),
    url(r'^FrameworkModules/PermissionSet/UserRoleBatchSet/', PermissionSet.UserRoleBatchSet),
    url(r'^FrameworkModules/PermissionSet/UserPermissionBatchSet/', PermissionSet.UserPermissionBatchSet),
    url(r'^FrameworkModules/PermissionSet/PermissionScopForm/', PermissionSet.PermissionScopForm),
    url(r'^FrameworkModules/PermissionSet/RoleUserBatchSet/', PermissionSet.RoleUserBatchSet),
    url(r'^FrameworkModules/PermissionSet/GetRoleUserIds/', PermissionSet.GetRoleUserIds),
    url(r'^FrameworkModules/PermissionSet/AddRoleUser/', PermissionSet.AddRoleUser),
    url(r'^FrameworkModules/PermissionSet/RemoveRoleUser/', PermissionSet.RemoveRoleUser),
    url(r'^FrameworkModules/PermissionSet/RolePermissionBatchSet/', PermissionSet.RolePermissionBatchSet),
    url(r'^FrameworkModules/PermissionSet/PermissionScopForm/', PermissionSet.PermissionScopForm),
    #授权范围管理
    url(r'^FrameworkModules/ResourcePermission/GetScopeUserIdsByUserId/', ResourcePermission.GetScopeUserIdsByUserId),
    url(r'^FrameworkModules/ResourcePermission/GetScopeRoleIdsByUserId/', ResourcePermission.GetScopeRoleIdsByUserId),
    url(r'^FrameworkModules/ResourcePermission/GetScopeModuleIdsByUserId/', ResourcePermission.GetScopeModuleIdsByUserId),
    url(r'^FrameworkModules/ResourcePermission/GetScopePermissionItemIdsByUserId/', ResourcePermission.GetScopePermissionItemIdsByUserId),
    url(r'^FrameworkModules/ResourcePermission/GetScopeOrganizeIdsByUserId/',
        ResourcePermission.GetScopeOrganizeIdsByUserId),
    url(r'^FrameworkModules/ResourcePermission/SaveUserUserScope/',
        ResourcePermission.SaveUserUserScope),
    url(r'^FrameworkModules/ResourcePermission/SaveUserRoleScope/',
        ResourcePermission.SaveUserRoleScope),
    url(r'^FrameworkModules/ResourcePermission/SaveOrganizeScope/',
        ResourcePermission.SaveOrganizeScope),
    url(r'^FrameworkModules/ResourcePermission/SaveModuleScope/',
        ResourcePermission.SaveModuleScope),
    url(r'^FrameworkModules/ResourcePermission/SavePermissionItemScope/',
        ResourcePermission.SavePermissionItemScope),
    url(r'^FrameworkModules/ResourcePermission/GetScopeRoleIdsByRoleId/',
        ResourcePermission.GetScopeRoleIdsByRoleId),
    url(r'^FrameworkModules/ResourcePermission/GetScopeUserIdsByRoleId/',
        ResourcePermission.GetScopeUserIdsByRoleId),
    url(r'^FrameworkModules/ResourcePermission/GetScopeOrganizeIdsByRoleId/',
        ResourcePermission.GetScopeOrganizeIdsByRoleId),
    url(r'^FrameworkModules/ResourcePermission/GetScopeModuleIdsByRoleId/',
        ResourcePermission.GetScopeModuleIdsByRoleId),
    url(r'^FrameworkModules/ResourcePermission/GetScopePermissionItemIdsByRoleId/',
        ResourcePermission.GetScopePermissionItemIdsByRoleId),
    url(r'^FrameworkModules/ResourcePermission/SaveRoleUserScope/',
        ResourcePermission.SaveRoleUserScope),
    url(r'^FrameworkModules/ResourcePermission/SaveRoleRoleScope/',
        ResourcePermission.SaveRoleRoleScope),
    url(r'^FrameworkModules/ResourcePermission/SaveRoleOrganizeScope/',
        ResourcePermission.SaveRoleOrganizeScope),
    url(r'^FrameworkModules/ResourcePermission/SaveRoleModuleScope/',
        ResourcePermission.SaveRoleModuleScope),
    url(r'^FrameworkModules/ResourcePermission/SaveRolePermissionItemScope/',
        ResourcePermission.SaveRolePermissionItemScope),

    url(r'^FrameworkModules/SysConfig/Index/',
        SysConfig.Index),
    url(r'^FrameworkModules/SysConfig/GetDefaultConfig/',
        SysConfig.GetDefaultConfig),
    url(r'^FrameworkModules/SysConfig/UpdateUserConfig/',
        SysConfig.UpdateUserConfig),


    url(r'^FrameworkModules/Highcharts/Sample1/', Highcharts.Sample1),
    url(r'^FrameworkModules/Highcharts/Sample2/', Highcharts.Sample2),
    url(r'^FrameworkModules/Highcharts/Sample3/', Highcharts.Sample3),
    url(r'^FrameworkModules/Highcharts/Sample4/', Highcharts.Sample4),
    url(r'^FrameworkModules/Highcharts/Sample5/', Highcharts.Sample5),
    url(r'^FrameworkModules/Highcharts/Sample6/', Highcharts.Sample6),
    url(r'^FrameworkModules/Highcharts/Sample7/', Highcharts.Sample7),
    url(r'^FrameworkModules/Highcharts/Sample8/', Highcharts.Sample8),
    url(r'^FrameworkModules/Highcharts/Sample9/', Highcharts.Sample9),
    url(r'^FrameworkModules/Highcharts/Sample10/', Highcharts.Sample10),
    url(r'^FrameworkModules/Highcharts/Sample11/', Highcharts.Sample11),
    url(r'^FrameworkModules/Highcharts/Sample12/', Highcharts.Sample12),
    url(r'^FrameworkModules/Highcharts/Sample13/', Highcharts.Sample13),
    url(r'^FrameworkModules/Highcharts/Sample14/', Highcharts.Sample14),
    url(r'^FrameworkModules/Highcharts/Sample15/', Highcharts.Sample15),
    url(r'^FrameworkModules/Highcharts/Sample16/', Highcharts.Sample16),
    url(r'^FrameworkModules/Highcharts/Sample17/', Highcharts.Sample17),
    url(r'^FrameworkModules/Highcharts/Sample18/', Highcharts.Sample18),
    url(r'^FrameworkModules/Highcharts/Sample19/', Highcharts.Sample19),
    url(r'^FrameworkModules/Highcharts/Sample20/', Highcharts.Sample20),
    url(r'^FrameworkModules/Highcharts/Sample21/', Highcharts.Sample21),
    url(r'^FrameworkModules/Highcharts/Sample22/', Highcharts.Sample22),
    url(r'^FrameworkModules/Highcharts/Sample23/', Highcharts.Sample23),
    url(r'^FrameworkModules/Highcharts/Sample24/', Highcharts.Sample24),
    url(r'^FrameworkModules/Highcharts/Sample25/', Highcharts.Sample25),
    url(r'^FrameworkModules/Highcharts/Sample26/', Highcharts.Sample26),
    url(r'^FrameworkModules/Highcharts/Sample27/', Highcharts.Sample27),
    url(r'^FrameworkModules/Highcharts/Sample28/', Highcharts.Sample28),
    url(r'^FrameworkModules/Highcharts/Sample29/', Highcharts.Sample29),

    url(r'^ExampleModules/PDFReader/Index/', PDFReader.Index),
    url(r'^ExampleModules/PDFReader/PDFViewer/', PDFReader.PDFViewer),
    url(r'^ExampleModules/CKEditor/Index/', CKEditor.Index),


]