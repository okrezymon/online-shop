<?php
/* Smarty version 3.1.39, created on 2021-11-11 19:29:50
  from 'C:\xampp\htdocs\kursy-online\modules\bluepayment\views\templates\admin\_configure\helpers\list\list_footer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_618d611e7a2806_38949615',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '31d13cf77f7a7b7c81836482fac0db387aaf67cc' => 
    array (
      0 => 'C:\\xampp\\htdocs\\kursy-online\\modules\\bluepayment\\views\\templates\\admin\\_configure\\helpers\\list\\list_footer.tpl',
      1 => 1636655308,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_618d611e7a2806_38949615 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, false);
?>
</table>
</div>
<div class="row">
	<div class="col-lg-6">
		<?php if ($_smarty_tpl->tpl_vars['bulk_actions']->value && $_smarty_tpl->tpl_vars['has_bulk_actions']->value) {?>
		<div class="btn-group bulk-actions dropup">
			<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" <?php if ($_smarty_tpl->tpl_vars['table']->value) {?>id="bulk_action_menu_<?php echo $_smarty_tpl->tpl_vars['table']->value;?>
"<?php }?>>
				<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Bulk actions','d'=>'Admin.Global'),$_smarty_tpl ) );?>
 <span class="caret"></span>
			</button>
			<ul class="dropdown-menu">
				<li>
					<a href="#" onclick="javascript:checkDelBoxes($(this).closest('form').get(0), '<?php echo $_smarty_tpl->tpl_vars['list_id']->value;?>
Box[]', true);return false;">
						<i class="icon-check-sign"></i>&nbsp;<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Select all','d'=>'Admin.Global'),$_smarty_tpl ) );?>

					</a>
				</li>
				<li>
					<a href="#" onclick="javascript:checkDelBoxes($(this).closest('form').get(0), '<?php echo $_smarty_tpl->tpl_vars['list_id']->value;?>
Box[]', false);return false;">
						<i class="icon-check-empty"></i>&nbsp;<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Unselect all','d'=>'Admin.Global'),$_smarty_tpl ) );?>

					</a>
				</li>
				<li class="divider"></li>
				<?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['bulk_actions']->value, 'params', false, 'key');
$_smarty_tpl->tpl_vars['params']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['key']->value => $_smarty_tpl->tpl_vars['params']->value) {
$_smarty_tpl->tpl_vars['params']->do_else = false;
?>
					<li<?php if ($_smarty_tpl->tpl_vars['params']->value['text'] == 'divider') {?> class="divider"<?php }?>>
						<?php if ($_smarty_tpl->tpl_vars['params']->value['text'] != 'divider') {?>
						<a href="#" onclick="<?php if ((isset($_smarty_tpl->tpl_vars['params']->value['confirm']))) {?>if (confirm('<?php echo $_smarty_tpl->tpl_vars['params']->value['confirm'];?>
'))<?php }?>sendBulkAction($(this).closest('form').get(0), 'submitBulk<?php echo $_smarty_tpl->tpl_vars['key']->value;
echo $_smarty_tpl->tpl_vars['table']->value;?>
');">
							<?php if ((isset($_smarty_tpl->tpl_vars['params']->value['icon']))) {?><i class="<?php echo $_smarty_tpl->tpl_vars['params']->value['icon'];?>
"></i><?php }?>&nbsp;<?php echo $_smarty_tpl->tpl_vars['params']->value['text'];?>

						</a>
						<?php }?>
					</li>
				<?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
			</ul>
		</div>
		<?php }?>
	</div>
</div>
<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_1267175381618d611e790638_48233352', "footer");
?>

<?php if (!$_smarty_tpl->tpl_vars['simple_header']->value) {?>
		<input type="hidden" name="token" value="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['token']->value,'html','UTF-8' ));?>
" />
	</div>
<?php } else { ?>
	</div>
<?php }?>

<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>'displayAdminListAfter'),$_smarty_tpl ) );?>

<?php if ((isset($_smarty_tpl->tpl_vars['name_controller']->value))) {?>
	<?php $_smarty_tpl->smarty->ext->_capture->open($_smarty_tpl, 'hookName', 'hookName', null);?>display<?php echo ucfirst($_smarty_tpl->tpl_vars['name_controller']->value);?>
ListAfter<?php $_smarty_tpl->smarty->ext->_capture->close($_smarty_tpl);?>
	<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>$_smarty_tpl->tpl_vars['hookName']->value),$_smarty_tpl ) );?>

<?php } elseif ((isset($_GET['controller']))) {?>
	<?php $_smarty_tpl->smarty->ext->_capture->open($_smarty_tpl, 'hookName', 'hookName', null);?>display<?php echo htmlentities(ucfirst($_GET['controller']));?>
ListAfter<?php $_smarty_tpl->smarty->ext->_capture->close($_smarty_tpl);?>
	<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>$_smarty_tpl->tpl_vars['hookName']->value),$_smarty_tpl ) );?>

<?php }?>

<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_2062090357618d611e7a0d53_60591909', "endForm");
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_457586711618d611e7a1655_04131332', "after");
?>

<?php }
/* {block "footer"} */
class Block_1267175381618d611e790638_48233352 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'footer' => 
  array (
    0 => 'Block_1267175381618d611e790638_48233352',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

<?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['toolbar_btn']->value, 'btn', false, 'k');
$_smarty_tpl->tpl_vars['btn']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['k']->value => $_smarty_tpl->tpl_vars['btn']->value) {
$_smarty_tpl->tpl_vars['btn']->do_else = false;
?>
	<?php if ($_smarty_tpl->tpl_vars['k']->value == 'back') {?>
		<?php $_smarty_tpl->_assignInScope('back_button', $_smarty_tpl->tpl_vars['btn']->value);?>
		<?php break 1;?>
	<?php }
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);
if ((isset($_smarty_tpl->tpl_vars['back_button']->value))) {?>
<div class="panel-footer">
	<a id="desc-<?php echo $_smarty_tpl->tpl_vars['table']->value;?>
-<?php if ((isset($_smarty_tpl->tpl_vars['back_button']->value['imgclass']))) {
echo $_smarty_tpl->tpl_vars['back_button']->value['imgclass'];
} else {
echo $_smarty_tpl->tpl_vars['k']->value;
}?>" class="btn btn-default<?php if ((isset($_smarty_tpl->tpl_vars['back_button']->value['target'])) && $_smarty_tpl->tpl_vars['back_button']->value['target']) {?> _blank<?php }?>"<?php if ((isset($_smarty_tpl->tpl_vars['back_button']->value['href']))) {?> href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['back_button']->value['href'],'html','UTF-8' ));?>
"<?php }
if ((isset($_smarty_tpl->tpl_vars['back_button']->value['js'])) && $_smarty_tpl->tpl_vars['back_button']->value['js']) {?> onclick="<?php echo $_smarty_tpl->tpl_vars['back_button']->value['js'];?>
"<?php }?>>
		<i class="process-icon-back <?php if ((isset($_smarty_tpl->tpl_vars['back_button']->value['class']))) {
echo $_smarty_tpl->tpl_vars['back_button']->value['class'];
}?>" ></i> <span <?php if ((isset($_smarty_tpl->tpl_vars['back_button']->value['force_desc'])) && $_smarty_tpl->tpl_vars['back_button']->value['force_desc'] == true) {?> class="locked" <?php }?>><?php echo $_smarty_tpl->tpl_vars['back_button']->value['desc'];?>
</span>
	</a>
</div>
<?php }
}
}
/* {/block "footer"} */
/* {block "endForm"} */
class Block_2062090357618d611e7a0d53_60591909 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'endForm' => 
  array (
    0 => 'Block_2062090357618d611e7a0d53_60591909',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

</form>
<?php
}
}
/* {/block "endForm"} */
/* {block "after"} */
class Block_457586711618d611e7a1655_04131332 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'after' => 
  array (
    0 => 'Block_457586711618d611e7a1655_04131332',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
}
}
/* {/block "after"} */
}
