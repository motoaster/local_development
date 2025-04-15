
<template>
<!-- HTMLを記載 -->
    <div id="example">
        <h1>Hello, Vue with Vite!</h1>
        <h2>~~~ {{ message }} ~~~</h2>
    </div>
</template>

<script>
// JSの処理を記載
import { ref } from 'vue'
const message = ref('Hello World!')
console.log(message)
console.log("test")
export default {
    data() {
        return {
            message
        }
    }
}
</script>


<style scoped>
/* 該当するCSSを記載 ※CSSファイルを別途読み込む場合は別 */
/* あくまでこの処理の表記に関するCSSのみを記載する */
h1, h2 {
    color: #fff;
    text-align: center;
}
#example {
    width: 50vh;
    margin: 1em auto;
    background-color: rgb(20, 20, 20, 1.0);
    padding: 2em;
    border:solid 2px #000;
    border-radius: 0.5em;
}
</style>
