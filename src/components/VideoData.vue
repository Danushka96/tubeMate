<template>
  <div>
    <v-card
        elevation="4"
    >
      <v-row>
        <v-col
            cols="12"
            sm="4"
        >
          <v-img
              lazy-src="https://picsum.photos/id/11/10/6"
              :src=video.thumbnail
          ></v-img>
        </v-col>
        <v-col
            cols="12"
            sm="7"
            class="mx-1"
        >
          <p>Title : {{ video.title }}</p>
          <p>Time : {{ Math.round(video.duration / 60) }} min</p>
          <p>Description :
            {{ (video.description.length > 60) ? video.description.substring(0, 60) : video.description }}</p>
          <v-row>
            <v-col
                class="d-flex"
                cols="12"
                sm="6"
            >
              <v-select
                  v-model="quality"
                  :items="getVideFormats()"
                  item-text="format"
                  item-value="format_id"
                  label="Quality"
                  outlined
              ></v-select>
            </v-col>
            <v-col
                cols="6"
                sm="3"
            >
              <a :href=getVideData() style="text-decoration:none;" target="_blank">
                <v-btn
                    :disabled="quality === null"
                    :loading="loading3"
                    class="ma-2 white--text"
                    color="green"
                >
                  Download
                  <v-icon
                      right
                  >
                    mdi-cloud-download
                  </v-icon>
                </v-btn>
              </a>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "VideoData",
  props: ['video'],
  data: () => ({
    loading3: false,
    items: [],
    quality: null
  }),
  methods: {
    getVideData() {
      return this.video.formats.filter(format => format.format_id === this.quality).map(format => format.url);
    },
    getVideFormats(){
      return this.video.formats.filter(format => format.abr)
    }
  }
}
</script>

<style scoped>

</style>
