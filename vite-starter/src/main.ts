import { createApp } from "vue";
import { Notify,Popup,Field,CellGroup,Tag } from 'vant';
import { Tabbar, TabbarItem } from 'vant';
import App from "./App.vue";
import axios from "axios";
import NutUI from "@nutui/nutui";
import router from "./router";
import "@nutui/nutui/dist/style.css";
import 'vant/lib/index.css'

// import "~/styles/element/index.scss";

// import ElementPlus from "element-plus";
// import all element css, uncommented next line
// import "element-plus/dist/index.css";

// or use cdn, uncomment cdn link in `index.html`
// If you want to use ElMessage, import it.
import "element-plus/theme-chalk/src/message.scss";

axios.defaults.baseURL='https://124.70.41.167:5000';
axios.defaults.timeout=45000;
const app = createApp(App);
// app.use(ElementPlus);
app.use(router).use(NutUI).use(Tag);
app.use(Notify).use(Field).use(CellGroup);
app.use(Popup).use(Tabbar).use(TabbarItem);
app.config.globalProperties.$axios = axios;
app.mount("#app");
