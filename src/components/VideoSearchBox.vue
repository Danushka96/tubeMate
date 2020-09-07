<template>
  <div>
    <v-row align="center" justify="center">
      <v-col
          cols="12"
          sm="8"
      >
        <v-text-field
            hint="https://www.youtube.com/watch?v=SzhLFazz7xU"
            label="Youtube Link"
            outlined
            persistent-hint
            v-model=videoUrl
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row align="center" justify="center" style="margin-top: -2rem">
      <v-col
          cols="6"
          sm="2"
      >
        <v-btn
            :disabled="loading"
            :loading="loading"
            class="ma-2 white--text"
            color="blue-grey"
            @click="getVideoInfo()"
        >
          Process
          <v-icon
              right
          >
            mdi-cloud-download
          </v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-snackbar
        v-model="error"
        top
        right
    >
      {{ errorText }}

      <template v-slot:action="{ attrs }">
        <v-btn
            color="red"
            text
            v-bind="attrs"
            @click="error = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "VideoSearchBox",
  data() {
    return {
      loading: false,
      videoUrl: '',
      error: false,
      errorText: '',
    }
  },
  methods: {
    getVideoInfo(){
      this.loading = true;
      axios.get("/api/info?video=" + this.videoUrl)
      .then(response => {
        if (response.data.error){
          this.error = true;
          this.loading = false;
          this.errorText = response.data.message
        } else {
          this.loading = false
          if (response.data._type){
            this.$store.commit('setVideoList', response.data.entries)
          }else{
            this.$store.commit('setVideoData', response.data)
          }
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
