import sharp from 'sharp';
import pngToIco from 'png-to-ico';
import { promises as fs } from 'fs';

async function generateImages() {
  try {
    const inputSvg = 'app/static/favicon.svg';
    const outputDir = 'app/static';

    // Generate all PNG sizes
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
    await fs.writeFile(`${outputDir}/favicon.ico`, buf);

    // Clean up temporary files
    await Promise.all([
      fs.unlink(`${outputDir}/temp-16.png`),
      fs.unlink(`${outputDir}/temp-32.png`)
    ]);

    console.log('All files generated successfully!');
  } catch (error) {
    console.error('Error:', error);
  }
}

generateImages();