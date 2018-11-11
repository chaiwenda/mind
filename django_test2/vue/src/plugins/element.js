import Vue from 'vue'
import CollapseTransition from 'element-ui/lib/transitions/collapse-transition'
import {
    Button,
    Aside,
    Main,
    Menu,
    Submenu,
    MenuItem,
    MenuItemGroup,
    Autocomplete,
    Slider,
    Container,
    Select,
    Option,
    OptionGroup,
    Loading,
    Message,
    Card,
    Pagination
} from 'element-ui'

Vue.use(Button);
Vue.use(Aside);
Vue.use(Main);
Vue.use(Menu);
Vue.use(Submenu);
Vue.use(MenuItem);
Vue.use(MenuItemGroup);
Vue.use(Autocomplete);
Vue.use(Slider);
Vue.use(Container);
Vue.use(Select);
Vue.use(Option);
Vue.use(OptionGroup);
Vue.use(Loading);
Vue.use(Card);
Vue.use(Pagination);

Vue.prototype.$message = Message;
Vue.component(CollapseTransition.name, CollapseTransition)

