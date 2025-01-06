import sharp from 'sharp';
import pngToIco from 'png-to-ico';
import { promises as fs } from 'fs';
import dotenv from 'dotenv';

dotenv.config();

const APP_NAME = process.env.APP_NAME || 'Flask Basics';

async function generateFaviconImages() {
  try {
    const inputSvg = 'src/favicon.svg';
    const outputDir = 'app/static/assets/favicon';

    // Ensure output directory exists
    await fs.mkdir(outputDir, { recursive: true });

    // Copy original SVG file
    await fs.copyFile(inputSvg, `${outputDir}/favicon.svg`);

    const sizes = [
      { size: 512, name: 'web-app-manifest-512x512.png' },
      { size: 192, name: 'web-app-manifest-192x192.png' },
      { size: 180, name: 'apple-touch-icon.png' },
      { size: 96, name: 'favicon-96x96.png' },
      { size: 32, name: 'temp-32.png' },  // For ICO
      { size: 16, name: 'temp-16.png' }   // For ICO
    ];

    console.log('Generating favicon images...');

    // Generate all PNGs
    await Promise.all(sizes.map(({ size, name }) =>
      sharp(inputSvg)
        .resize(size, size)
        .png()
        .toFile(`${outputDir}/${name}`)
    ));

    // Generate ICO from 16x16 and 32x32 PNGs
    const buf = await pngToIco([
      `${outputDir}/temp-16.png`,
      `${outputDir}/temp-32.png`
    ]);
    await fs.writeFile(`app/static/favicon.ico`, buf);

    // Clean up temporary files
    await Promise.all([
      fs.unlink(`${outputDir}/temp-16.png`),
      fs.unlink(`${outputDir}/temp-32.png`)
    ]);

    // Generate the manifest file
    const manifest = {
      "name": APP_NAME,
      "short_name": APP_NAME,
      "icons": [
        {
          "src": "/assets/favicon/web-app-manifest-192x192.png",
          "sizes": "192x192",
          "type": "image/png",
          "purpose": "maskable"
        },
        {
          "src": "/assets/favicon/web-app-manifest-512x512.png",
          "sizes": "512x512",
          "type": "image/png",
          "purpose": "maskable"
        }
      ],
      "theme_color": "#FFFFFF",
      "background_color": "#FFFFFF",
      "display": "standalone"
    };

    // Write the manifest file
    await fs.writeFile(
      'app/static/site.webmanifest',
      JSON.stringify(manifest, null, 2),
      'utf8'
    );

    console.log('All favicon files generated successfully!');
  } catch (error) {
    console.error('Error:', error);
  }
}

generateFaviconImages();