/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Component } from "@odoo/owl";

patch(Component.prototype, {
    setup() {
        super.setup?.();

        // attendre DOM ready POS
        setTimeout(() => {
            const btn = document.querySelector(".cashier-name");

            if (btn) {
                btn.addEventListener("click", (ev) => {
                    ev.preventDefault();
                    ev.stopPropagation();
                }, true);
            }
        }, 1000);
    },
});