import sharp from 'sharp';
import { promises as fs } from 'fs';

async function generateSocialImages() {
  try {
    const inputSvg = 'src/social.svg';
    const outputDir = 'app/static/assets/social';
    const backgroundColor = process.argv[2] || '#FFFFFF';

    // Ensure output directory exists
    await fs.mkdir(outputDir, { recursive: true });

    const sizes = [
      { width: 1200, height: 630, name: 'og-image.png' },
      { width: 1200, height: 630, name: 'twitter-card.png' }
    ];

    console.log('Generating social media cards...');
    console.log(`Using background color: ${backgroundColor}`);

    await Promise.all(sizes.map(({ width, height, name }) =>
      sharp(inputSvg)
        .resize(width, height, { fit: 'contain', background: backgroundColor })
        .flatten({ background: backgroundColor })
        .png()
        .toFile(`${outputDir}/${name}`)
    ));

    console.log('All social cards generated successfully!');
  } catch (error) {
    console.error('Error:', error);
  }
}

generateSocialImages();