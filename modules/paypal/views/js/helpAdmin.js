/*! For license information please see helpAdmin.js.LICENSE */
!function(t){var e={};function n(o){if(e[o])return e[o].exports;var a=e[o]={i:o,l:!1,exports:{}};return t[o].call(a.exports,a,a.exports,n),a.l=!0,a.exports}n.m=t,n.c=e,n.d=function(t,e,o){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:o})},n.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)n.d(o,a,function(e){return t[e]}.bind(null,a));return o},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="",n(n.s=11)}({0:function(t,e,n){"use strict";n.d(e,"a",(function(){return o})),n.d(e,"b",(function(){return a}));var o=function(t){$(".defaultForm").removeClass("pp-settings-link-on"),$(".page-head-tabs a").removeClass("pp-settings-link-on pp__border-b-primary"),t.addClass("pp-settings-link-on"),$("html, body").animate({scrollTop:t.offset().top-200+"px"},900)},a=function(){var t=document.querySelectorAll(".page-head-tabs a"),e=$(".page-head-tabs a.current");t.forEach((function(t){var n=$(t).attr("href").includes("AdminPayPalCustomizeCheckout"),o=$(t).attr("href").includes("AdminPayPalSetup");(e.attr("href").includes("AdminPayPalCustomizeCheckout")&&o||e.attr("href").includes("AdminPayPalSetup")&&n)&&$(t).addClass("pp-settings-link-on pp__border-b-primary")})),$("html, body").animate({scrollTop:$(".page-head-tabs").offset().top-200+"px"},900)}},11:function(t,e,n){"use strict";n.r(e);var o=n(2),a={init:function(){$("#ckeck_requirements").click((function(){a.checkCredentials()})),$(".install-ps-checkout").click((function(){o.SetupAdmin.psCheckoutHandleAction("install")}))},checkCredentials:function(){$.ajax({url:controllerUrl,type:"POST",dataType:"JSON",data:{ajax:!0,action:"CheckCredentials"},success:function(t){var e,n;for(var o in $(".action_response").html(""),n=1==t.success?"success":"danger",t.message)e=a.getAlert(t.message[o],n),$(e).appendTo(".action_response")}})},getAlert:function(t,e){var n=document.createElement("div"),o=document.createElement("div");return o.innerHTML=t,n.className="alert alert-".concat(e),n.appendChild(o),n}};document.addEventListener("DOMContentLoaded",(function(){a.init()}))},2:function(t,e,n){"use strict";n.r(e),n.d(e,"SetupAdmin",(function(){return r}));var o=n(0),a=function(t,e){$.ajax({url:controllerUrl,type:"POST",data:{ajax:!0,action:"handleOnboardingResponse",authCode:t,sharedId:e},success:function(t){console.log(t)}})},r={init:function(){$("#logoutAccount").on("click",(function(t){r.logoutAccount()})),$("#confirmCredentials").click((function(t){$(t.currentTarget).closest("form").submit()})),$(document).on("click","#btn-check-requirements",(function(){r.checkRequirements()})),$("[data-pp-link-settings]").on("click",(function(t){t.preventDefault();var e=$(t.target.attributes.href.value);e.length?Object(o.a)(e):Object(o.b)()})),$(".defaultForm").on("mouseleave",(function(t){$(t.currentTarget).removeClass("pp-settings-link-on")})),$(".ps-checkout-info").on("click",(function(t){var e=t.target.getAttribute("data-action");r.psCheckoutHandleAction(e)})),$(document).on("contextmenu","[data-paypal-button]",(function(t){t.preventDefault()})),window.onboardCallback=a,$("[data-update-rounding-settings]").on("click",(function(t){r.updateRoundingSettings(t)})),$("[data-show-rounding-alert]").on("click",(function(t){var e=$("[data-rounding-alert]");e.removeClass("hidden");var n=e.offset().top-$(".page-head").height()-45;$("html, body").animate({scrollTop:n},500)}))},logoutAccount:function(){$.ajax({url:controllerUrl,type:"POST",data:{ajax:!0,action:"logOutAccount"},success:function(t){t.status&&(document.location=t.redirectUrl)}})},checkRequirements:function(){$.ajax({url:controllerUrl,type:"POST",data:{ajax:!0,action:"CheckCredentials"},success:function(t){$("#btn-check-requirements").closest(".status-block-container").html(t)}})},psCheckoutHandleAction:function(t){null!=t&&$.ajax({url:controllerUrl,type:"POST",data:{ajax:!0,action:"HandlePsCheckoutAction",actionHandled:t},success:function(t){t.redirect&&window.open(t.url,"_blank")}})},updateRoundingSettings:function(t){$.ajax({url:controllerUrl,type:"POST",data:{ajax:!0,action:"UpdateRoundingSettings"},success:function(e){var n=$(t.currentTarget).closest("[data-rounding-alert]");n.length>0&&(n.removeClass("alert-warning").addClass("alert-success"),n.html(e),setTimeout((function(){return n.remove()}),5e3))}})}};window.addEventListener("load",(function(){return r.init()})),$(window).on("load",(function(){return $("[data-paypal-button]").removeClass("spinner-button")}))}});
//# sourceMappingURL=helpAdmin.js.map