<template>
  <div class="poll">
    <div class="poll-list" v-for="poll in polls" v-bind:key="poll.id">
      <div class="poll-card">
        <h1>{{ poll.title }}</h1>
        <p>{{ poll.description }}</p>
        <Options v-bind:options_url="poll.options" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Options from "@/components/Option";
const API_URL = 'http://127.0.0.1:8000/'



export default {
  name: 'HelloWorld',
  components: {Options},
  data () {
    return {
      polls: []
    }
  },
  mounted() {
    this.getPolls()
  },
  methods: {
    getPolls() {
      axios({
        method: 'get',
        url: API_URL + 'poll/',
        auth: {
          username: 'admin',
          password: 'admin'
        }
      }).then(response => this.polls = response.data)
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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
</style>
