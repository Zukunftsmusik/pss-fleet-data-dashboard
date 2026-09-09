<script setup>
import { ref, onMounted } from 'vue'

const message = ref('Connecting to PSS Fleet Data Backend...')
const environment = ref('')

onMounted(async () => {
  try {
    const response = await fetch('/dashboard/api/v1/test/')
    const result = await response.json()
    message.value = result.message
    environment.value = result.container_environment
  } catch (error) {
    message.value = 'System Gateway Offline'
  }
})
</script>

<template>
  <div class="vintage-body">
    <table align="center">
        <tr>
            <td>
                <img src="https://www.feuerwehr-hitzacker.de/OLD/blaulicht.gif" width="100" alt="Under Construction GIF" />
                <br />
                <img src="https://www.animatedimages.org/data/media/559/animated-light-image-0050.gif"/>
            </td>
            <td>
                <h1>⚠️ PSS FLEET DATA ⚠️</h1>
                <h2>*** DASHBOARD SYSTEM IS UNDER CONSTRUCTION ***</h2>
            </td>
            <td>
                <img src="https://www.feuerwehr-hitzacker.de/OLD/blaulicht.gif" width="100" alt="Under Construction GIF" />
                <br />
                <img src="https://www.animatedimages.org/data/media/559/animated-light-image-0050.gif"/>
            </td>
        </tr>
    </table>
                
    <marquee scrollamount="10">⚡⚡ WELCOME TO THE FUTURE -- LAUNCHING SOON -- STAY TUNED ⚡⚡</marquee>

    <!-- The classic Tenor construction GIF -->
    <table align="center" width="90%">
        <tr>
            <td>
                <img src="https://media.tenor.com/MRCIli40TYoAAAAj/under-construction90s-90s.gif" width="100" alt="Under Construction GIF" />
            </td>
            <td>
                <img src="https://www.animatedimages.org/data/media/695/animated-under-construction-image-0049.gif"/>
            </td>
            <td>
                <img src="https://media.tenor.com/MRCIli40TYoAAAAj/under-construction90s-90s.gif" width="100" alt="Under Construction GIF" />
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://www.animatedimages.org/data/media/695/animated-under-construction-image-0053.gif" />
                <br />
                <br />
                <img src="https://www.animatedimages.org/data/media/695/animated-under-construction-image-0055.gif"/>
            </td>
            <td>
                <div class="gif-container">
                    <img src="https://media1.tenor.com/m/nq76xNvyoYkAAAAd/construction-lol.gif" alt="Under Construction GIF" />
                </div>
            </td>
            <td>
                <img src="https://www.animatedimages.org/data/media/695/animated-under-construction-image-0055.gif"/>
                <br />
                <br />
                <img src="https://www.animatedimages.org/data/media/695/animated-under-construction-image-0059.gif" />
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://media.tenor.com/MRCIli40TYoAAAAj/under-construction90s-90s.gif" width="100" alt="Under Construction GIF" />
            </td>
            <td>

            </td>
            <td>
                <img src="https://media.tenor.com/MRCIli40TYoAAAAj/under-construction90s-90s.gif" width="100" alt="Under Construction GIF" />
            </td>
        </tr>
    </table>

    <table class="status-box">
        <tr>
            <td><strong>Gateway Status:</strong></td>
            <td>{{ message }}</td>
        </tr>
        <tr v-if="environment">
            <td><strong>Stack context:</strong></td>
            <td>{{ environment }}</td>
        </tr>
    </table>

    <p class="footer-text">Webmaster Contact: <a href="mailto:theworstpss@gmail.com">theworstpss@gmail.com</a></p>

    <div class="visitor-counter">
      VISITOR COUNT: 0001337
    </div>
  </div>
</template>

<style scoped>
.vintage-body {
  background-color: #ccc; /* Classic Windows Blue */
  color: #00FF00;           /* Terminal Green Text */
  font-family: "MS Sans Serif", "Courier New", monospace;
  text-align: center;
  padding: 50px;
  min-height: 100vh;
  box-sizing: border-box;
}

h1 {
  color: #FFCC00;
  font-size: 3em;
  text-shadow: 3px 3px #FF0000;
  margin-top: 0;
  margin-bottom: 10px;
}

h2 {
  font-size: 1.5em;
  margin-bottom: 30px;
}

marquee {
  background-color: #FF0000;
  color: #FFFFFF;
  font-weight: bold;
  padding: 10px;
  font-size: 1.2em;
  border: 3px outset #FFF;
  margin: 20px 0;
}

.gif-container {
  margin: 30px auto;
  max-width: 444px;
  border: 4px ridge #808080;
  background: #C0C0C0;
  padding: 10px;
}

.status-box {
  max-width: 500px;
  margin: 20px auto;
  border: 2px inset #808080;
  background: #000;
  padding: 10px;
  font-size: 0.9em;
}

.footer-text {
  margin-top: 40px;
}

.footer-text a {
  color: #00FFFF;
  text-decoration: underline;
}

.visitor-counter {
  font-size: 1.5em;
  color: #FFFFFF;
  background: #000000;
  border: 2px inset #808080;
  display: inline-block;
  padding: 5px 15px;
  margin-top: 20px;
}
</style>
