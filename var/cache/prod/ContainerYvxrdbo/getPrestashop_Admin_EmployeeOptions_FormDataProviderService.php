<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.admin.employee_options.form_data_provider' shared service.

return $this->services['prestashop.admin.employee_options.form_data_provider'] = new \PrestaShopBundle\Form\Admin\Configure\AdvancedParameters\Employee\EmployeeOptionsFormDataProvider(${($_ = isset($this->services['prestashop.core.team.employee.configuration.employee_options_configuration']) ? $this->services['prestashop.core.team.employee.configuration.employee_options_configuration'] : $this->load('getPrestashop_Core_Team_Employee_Configuration_EmployeeOptionsConfigurationService.php')) && false ?: '_'});