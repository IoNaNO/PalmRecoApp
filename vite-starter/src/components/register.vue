<script setup lang="ts">
import { ref } from "vue";
import { Notify } from '@nutui/nutui'
import console from "console";
import axios from "axios";

const left_images = ref([]);
const right_images = ref([]);
const isloading = ref(false);

const picnum = 2;
const username = ref("");
const left_cnt = ref(0);
const right_cnt = ref(0);
const left_cam = async () => {

    let num = picnum - left_cnt.value;
    if (num == 0) {
        Notify.primary('Already Done');
        return;
    }
    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        Notify.primary(navigator.camera);
    }
    try {
        // Make sure Cordova is ready
        if (window.cordova) {
            const options = {
                quality: 25,
                destinationType: Camera.DestinationType.DATA_URL,
                sourceType: Camera.PictureSourceType.CAMERA,
                encodingType: Camera.EncodingType.JPEG,
                mediaType: Camera.MediaType.PICTURE
            };
            async function takePicture(options) {
                return new Promise((resolve, reject) => {
                    navigator.camera.getPicture(resolve, reject, options);
                });
            }
            // Get result by camera
            for (let i = 0; i < num; i++) {
                const imageData = await takePicture(options);
                left_images.value.push('data:image/jpeg;base64,'+imageData);    // base64header is necessary
                left_cnt.value++;
            }
        } else {
            console.log('Cordova is not loaded');
        }
    } catch (error) {
        Notify.primary('Error opening camera', error);
    }
}
const right_cam = async () => {
    let num = picnum - right_cnt.value;
    if (num == 0) {
        Notify.primary('Already Done');
        return;
    }
    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        Notify.primary(navigator.camera);
    }
    try {
            // Make sure Cordova is ready
        if (window.cordova) {
            const options = {
                quality: 25,
                destinationType: Camera.DestinationType.DATA_URL,
                sourceType: Camera.PictureSourceType.CAMERA,
                encodingType: Camera.EncodingType.JPEG,
                mediaType: Camera.MediaType.PICTURE
            };

            async function takePicture(options) {
                return new Promise((resolve, reject) => {
                    navigator.camera.getPicture(resolve, reject, options);
                });
            }
            // get result by camera
            for (let i = 0; i < num; i++) {
                const imageData = await takePicture(options);
                right_images.value.push('data:image/jpeg;base64,'+imageData);
                right_cnt.value++;
            }
        } else {
            console.log('Cordova is not loaded');
        }
    } catch (error) {
        Notify.primary('Error opening camera', error);
    }
}
const register = () => {
    if (username.value == "") {
        Notify.warn("Please input username");
        return;
    }
    if (left_cnt.value != picnum || right_cnt.value != picnum) {
        Notify.warn("Please take enough photos");
        return;
    }
    // send to server
    isloading.value = true;
    let config = {
        method: 'post',
        url: "/register",
        headers: {
            'Content-Type': 'application/json'
        },
        data: {
            username: username.value,
            left_images: left_images.value,
            right_images: right_images.value
        }
    };
    axios(config).then((res) => {
        isloading.value = false;
        if (res.data.code == 0) {
            Notify.success("Register Success");
        } else {
            Notify.danger("Register Failed");
        }
        left_cnt.value = 0;
        right_cnt.value = 0;
        left_images.value = [];
        right_images.value = [];
    }).catch((err) => {
        isloading.value = false;
        Notify.danger(err);
    });

}
</script>

<template>
    <div>
        <span>Image count:</span>
        <van-tag type="primary" size="large" class="tag">LeftHand:{{ left_cnt }}</van-tag>
        <van-tag type="primary" size="large">RightHand:{{ right_cnt }}</van-tag>
    </div>

    <div class="funitem">
        <func msg="LeftHand" @click="left_cam"></func>
    </div>
    <div class="funitem">
        <func msg="RightHand" @click="right_cam"></func>
    </div>
    <van-cell-group inset style="justify-content: center; display: flex;">
        <van-field v-model="username" label="Username" placeholder="Your Username" class="inputbox" />
    </van-cell-group>
    <div class="funitem">
        <func msg="Register" background-color="#749938" text-color="white" @click="register"></func>
    </div>
    <div v-if="isloading">
        <nut-icon name="loading1"></nut-icon>
    </div>
</template>

<style scoped>
.ep-button {
    margin: 4px;
}

.ep-button+.ep-button {
    margin-left: 0;
    margin: 4px;
}

.funitem {
    display: flex;
    justify-content: center;
    align-items: center;
}

.imgcontainer {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 250px;
}

.tag {
    margin: 10px;
}

.centered-image {
    height: 200px;
    object-fit: contain;

}

.inputbox {
    border-radius: 10px;
    border: 1px solid #ccc;
    width: 100%;
}
</style>
