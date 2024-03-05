<script lang="ts" setup>

</script>

<template>
    <div class="topbar">
    <nut-navbar style="height:80px;line-height: 20px;margin-bottom: 0%;padding-left: 0%;">
      <template #content>
        <div class="logotitle logocolor"><b>PlamPrint</b></div>
      </template>
      <template #left>
      </template>
      <!-- <template #right>
        <div >
          <nut-badge :value="8">
            <nut-icon name="notice"></nut-icon>
          </nut-badge>
        </div>
      </template> -->
    </nut-navbar>
    </div>
</template>

<style scoped>
.logotitle {
  font-size: 35px;
}

.logocolor {
  color: #e23c13
}

.topbar{
    display: block;
    width: 100%;
}
</style>