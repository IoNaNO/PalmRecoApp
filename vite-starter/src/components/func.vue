<script setup lang="ts">
import { ref } from "vue";
const props = defineProps({
  msg: String,
  backgroundColor: {
    type: String,
    default: 'white'
  },
  textColor:{
    type: String,
    default: 'black'
  }
});
</script>

<template>
    <div class="card" :style="{ backgroundColor: backgroundColor }">
        <p :style="{color:textColor}">{{ msg }}</p>
    </div>
</template>

<style scoped>
.card {
  display: block;
  align-items: center;
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 10px;
  margin: 20px;
  box-shadow: 20px rgba(0,0,0,0.15);
  width: 80%;
}
</style>
