<template>
    <!-- <div class="topbar">
    <nut-navbar style="height:80px;line-height: 20px;margin-bottom: 0%;padding-left: 0%;">
      <template #content>
        <div class="logotitle logocolor"><b>PlamPrint</b></div>
      </template>
      <template #left>
      </template>
      <template #right>
        <div >
          <nut-badge :value="8">
            <nut-icon name="notice"></nut-icon>
          </nut-badge>
        </div>
      </template>
    </nut-navbar>
    </div>
    <router-view></router-view>
    <div class="top">
    </div> -->
    <div class="tabbar">
        <van-tabbar v-model="activeName" route active-color="#e23c13">
            <van-tabbar-item to="/register" icon="apps-o">Sign in</van-tabbar-item>
            <van-tabbar-item to="/home" icon="home-o">Home</van-tabbar-item>
        </van-tabbar>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const homedotflag = ref(false);
const activeName = ref('home');
</script>

<style scoped>


.tabbar {
    position: fixed;   /* 使用 fixed 而不是 absolute */
    bottom: 0;         /* 确保元素位于窗口底部 */
    width: 100%;       /* 确保元素宽度为全屏 */
    height: 50px;
    display: block;
}

.nut-tabbar-bottom {
    position: absolute;
}
</style>