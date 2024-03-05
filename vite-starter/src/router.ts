import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        name:'home',
        component: () => import('~/components/home.vue')
    },
    {
        path: '/register',
        name:'register',
        component: () => import('~/components/register.vue')
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
});

export default router