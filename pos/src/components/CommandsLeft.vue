<template>
<div class="buttons">
  <button class="payment">PAY</button>
  <button class="cancel" @click="clearKabeh">CANCEL</button>
</div>
</template>

<script>
export default {
  name: 'CommandsLeft',
  props : ['clearKabeh']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.buttons{
  display: flex;
  justify-content: space-around;
  padding-top:40px;
  padding-right:10px ;
}

button{
  border-radius: 30px;
  padding: 12px;
  font-size: 14px;
}
.payment{
  background-color: #05BD2D;
  color: white;
  border: hidden;
  width: 100px;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);
}

.cancel{
  background-color: rgba(218, 20, 14, 0.86);
  color: antiquewhite;
  border: hidden;
  width: 100px;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);

}
</style>
