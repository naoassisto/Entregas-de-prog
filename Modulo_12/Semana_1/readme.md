## Link para acesso: https://hail-cheerful-pisces.glitch.me/

**O que foi desenvolvido?**

Foi desenvolvida uma aplicação web que utiliza tecnologias de realidade aumentada (AR) e realidade virtual (VR) para proporcionar experiências imersivas ao usuário. A aplicação consiste em duas partes:

1. **Experiência de Realidade Virtual (VR):** Uma cena em 360 graus que permite ao usuário explorar um ambiente virtual utilizando a biblioteca A-Frame.
2. **Experiência de Realidade Aumentada (AR):** Uma cena que utiliza A-Frame e AR.js para exibir um modelo 3D quando um marcador específico é detectado pela câmera do dispositivo.

---

## **Como foi implementada a experiência de realidade aumentada?**

A experiência de realidade aumentada foi implementada utilizando as bibliotecas **A-Frame** e **AR.js**. O código HTML configura uma cena AR onde, ao apontar a câmera do dispositivo para um marcador predefinido, um modelo 3D é renderizado sobre ele. A implementação segue os seguintes passos:

1. **Inclusão das Bibliotecas Necessárias:**

   - **A-Frame:** Para criar e manipular a cena 3D.
   - **AR.js:** Para adicionar funcionalidades de AR à cena A-Frame.

   ```html
   <script src="https://aframe.io/releases/1.3.0/aframe.min.js"></script>
   <script src="https://raw.githack.com/AR-js-org/AR.js/3.4.5/three.js/build/ar-threex-location-only.js"></script>
   <script src="https://raw.githack.com/AR-js-org/AR.js/3.4.5/aframe/build/aframe-ar.js"></script>
   ```

2. **Configuração da Cena AR:**

   - A cena é criada com `<a-scene>`, desabilitando a interface de usuário de VR e de depuração do AR.js para uma experiência mais limpa.

   ```html
   <a-scene vr-mode-ui="enabled: false" arjs="debugUIEnabled:false">
     <!-- Conteúdo da cena -->
   </a-scene>
   ```

3. **Definição dos Assets:**

   - O modelo 3D a ser exibido é carregado nos assets para pré-carregamento.

   ```html
   <a-assets>
     <a-asset-item id="shiba" src="caminho/para/scene.gltf"></a-asset-item>
   </a-assets>
   ```

4. **Configuração do Marcador AR:**

   - Utiliza o marcador predefinido "hiro" para detectar quando o modelo 3D deve ser exibido.

   ```html
   <a-marker preset="hiro">
     <!-- Modelo 3D a ser renderizado -->
   </a-marker>
   ```

5. **Adição do Modelo 3D à Cena:**

   - O modelo é inserido dentro do marcador para que seja renderizado quando o marcador for detectado pela câmera.

   ```html
   <a-entity 
     gltf-model="#shiba" 
     position="0 0 0" 
     scale="0.02 0.02 0.02" 
     rotation="-90 0 0">
   </a-entity>
   ```

6. **Definição da Câmera:**

   - A câmera é adicionada à cena para capturar o vídeo e detectar o marcador.

   ```html
   <a-entity camera></a-entity>
   ```

**Funcionamento:**

- Quando o usuário aponta a câmera do dispositivo para o marcador "hiro", o AR.js detecta o marcador e a aplicação renderiza o modelo 3D sobre ele.
- O modelo pode ser visualizado em diferentes ângulos movendo o dispositivo ou o marcador.

---

## **Como foi implementada a experiência de realidade virtual?**

A experiência de realidade virtual foi implementada utilizando apenas a biblioteca **A-Frame** para criar uma cena 3D imersiva. A implementação inclui os seguintes elementos:

1. **Inclusão da Biblioteca A-Frame:**

   - Permite a criação de elementos 3D e interações na cena.

   ```html
   <script src="https://aframe.io/releases/1.6.0/aframe.min.js"></script>
   ```

2. **Configuração da Cena VR:**

   - A cena é criada com `<a-scene>`, que serve como contêiner para todos os elementos.

   ```html
   <a-scene>
     <!-- Elementos da cena VR -->
   </a-scene>
   ```

3. **Definição dos Assets:**

   - Recursos como imagens e sons são carregados antecipadamente.

   ```html
   <a-assets>
     <img id="img" src="caminho/para/sala.jpg" />
     <!-- Outros assets -->
   </a-assets>
   ```

4. **Criação do Ambiente 360 Graus:**

   - Um céu esférico é criado utilizando `<a-sky>` para envolver a cena com uma imagem 360 graus.

   ```html
   <a-sky src="#img"></a-sky>
   ```

5. **Adição de Elementos Interativos:**

   - Textos e objetos são adicionados à cena para enriquecer a experiência.

   ```html
   <a-text value="Exemplo" position="0 1 -3" color="#FF0000"></a-text>
   ```

6. **Configuração da Câmera e Cursor:**

   - A câmera define a posição e orientação inicial do usuário.
   - O cursor permite interações através do olhar.

   ```html
   <a-camera position="0 1.6 0">
     <a-cursor></a-cursor>
   </a-camera>
   ```

### **Funcionamento:**

- O usuário pode explorar o ambiente virtual movendo-se ou girando a visão.
- Elementos interativos podem responder a ações do usuário, como olhar fixamente para um objeto.



### **Resumo Geral:**

- **Realidade Aumentada (AR):** Implementada com A-Frame e AR.js, permitindo que um modelo 3D seja renderizado sobre um marcador detectado pela câmera.
- **Realidade Virtual (VR):** Criada usando apenas A-Frame, proporcionando um ambiente imersivo em 360 graus onde o usuário pode interagir com objetos virtuais.
